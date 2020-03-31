from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Assignment, Submission
import pytz
from datetime import datetime, timedelta
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
#from .forms import *

class DashboardListView(ListView):
    model = Assignment
    template_name = "dashboard/dashboard.html"

# @login_required
# def dashboard(request):
#     ass = Assignment.objects.filter(user=request.user)
#     # paginator = Paginator(article, 6) # < 3 is the number of items on each page
#     # page = request.GET.get('page') # < Get the page number
#     # ass = paginator.get_page(page) # < New in 2.0!
#     data = {}
#     data['object_list'] = ass
#     return render(request, 'dashboard/dashboard.html',data)

class AssignmentDetailView(DetailView):
    model = Assignment
    template_name = 'dashboard/assignment_detail.html'


class SubmissionCreateView(CreateView):
    model = Submission
    template_name = "dashboard/submission.html"
    fields = ['assignment_file', 'assignment_link', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        assign = Assignment.objects.get(id=self.kwargs['pk'])
        form.instance.assignment = assign
        return super(SubmissionCreateView, self).form_valid(form)

    @property
    def is_past_due(self):
        date = Assignment.objects.get(id=self.kwargs['pk'])
        now = pytz.utc.localize(datetime.utcnow().now()) - timedelta(hours=2)
        return now > date.due_date

    def get_context_data(self, **kwargs):
        context = super(SubmissionCreateView, self).get_context_data(**kwargs)
        context['deadline_passed'] = self.is_past_due
        return context


class SubmissionUpdateView(UpdateView):
    model = Submission
    template_name = "dashboard/submission.html"
    fields = ['user', 'assignment', 'assignment_file', 'assignment_url', 'description']


def it(request):
    ass_it = Assignment.objects.filter(department__name='Information Technology').order_by('-id')
    return render(request,'depart/it.html',{'ass_it':ass_it})

def _is(request):
    ass_is = Assignment.objects.filter(department__name='Information System').order_by('-id')
    return render(request,'depart/is.html',{'ass_is':ass_is})

def cs(request):
    ass_cs = Assignment.objects.filter(department__name='Computer Science').order_by('-id')
    return render(request,'depart/cs.html',{'ass_cs':ass_cs})


