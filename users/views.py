from django.shortcuts import render
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView

@login_required
def update_user(request):

    try:
        user_profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return HttpResponse("invalid user_profile!")

    if request.method == "POST":
        update_user_form = UserUpdateForm(data=request.POST, instance=request.user)
        update_profile_form = ProfileUpdateForm(data=request.POST, instance=user_profile)

        if update_user_form.is_valid() and update_profile_form.is_valid():
            user = update_user_form.save()
            profile = update_profile_form.save(commit=False)
            profile.user = user

            if 'image' in request.FILES:
                profile.image = request.FILES['image']

            profile.save()

        else:
            print(update_user_form.errors, update_profile_form.errors)
    else:
        update_user_form = UserUpdateForm(instance=request.user)
        update_profile_form = ProfileUpdateForm(instance=user_profile)

    return render(request,
            'user/update_profile.html',
            {'update_user_form': update_user_form, 'update_profile_form': update_profile_form}
            )


class LoginView(LoginView):
    def form_valid(self, form):
        login(self.request, user)
        if form.get_user().change_password:
            return HttpResponseRedirect(reverse('password_change'))
        else:
            auth_login(self.request, form.get_user())
            return HttpResponseRedirect(self.get_success_url())


 