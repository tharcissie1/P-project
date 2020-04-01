from django.urls import path
from .views import  AssignmentDetailView, SubmissionUpdateView, SubmissionCreateView, DashboardListView
from .import views
from django.contrib.auth import views as auth_views
from users import views as user_views




urlpatterns = [
    path('', DashboardListView.as_view(), name='dashboard'),
    path('assignments/<int:pk>', AssignmentDetailView.as_view(), name='assignment-detail'),
    path('assignments/<int:pk>/submission', SubmissionCreateView.as_view(), name='submit-assignment'),
    path('assignments/it', views.it, name='it'),
    path('assignments/is', views._is, name='is'),
    path('assignments/cs', views.cs, name='cs'),
    #path('', views.dashboard, name='dashboard'),
    path('update_user/', user_views.update_user, name='update_user'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('reset/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html',email_template_name='registration/password_reset_email.html',subject_template_name='registration/password_reset_subject.txt'),name='password_reset'),
    path('reset/done',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/complete/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),
    path('settings/password/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),name='password_change'),
    path('settings/password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),name='password_change_done'),
    
] 
