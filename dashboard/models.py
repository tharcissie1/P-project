from django.db import models
from django.contrib.auth.models import User
from users.models import Department
from django.urls import reverse
from django_userforeignkey.models.fields import UserForeignKey

from datetime import datetime, timedelta
import pytz
from django.utils import timezone


class Course(models.Model):
    name = models.CharField(max_length=200)
    year = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1, related_name="course_department")

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.name


class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_assignments")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1, related_name="department_assignments")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField()

    class Meta:
        verbose_name = "Assignment"
        verbose_name_plural = "Assignments"

    def __str__(self):
        return self.title

    @property
    def is_past_due(self):
        now = pytz.utc.localize(datetime.utcnow().now()) - timedelta(hours=2)
        return now > self.due_date

    def deadline(self):
        my_timezone = pytz.timezone("Africa/Kigali")
        return self.due_date.astimezone(my_timezone).strftime('%d-%b-%Y %H:%M')

    def created_date(self):
        my_timezone = pytz.timezone("Africa/Kigali")
        return self.created.astimezone(my_timezone).strftime('%d-%b-%Y %H:%M')


class Submission(models.Model):
    user     = UserForeignKey(auto_user_add=True, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    assignment_file = models.FileField(upload_to='assignments/', blank=True)
    assignment_link = models.URLField(blank=True)
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name = "Submission"
        verbose_name_plural = "Submissions"

    def __str__(self):
        return self.assignment.title + " " + self.user.email

    def get_absolute_url(self):
        return reverse('dashboard')
