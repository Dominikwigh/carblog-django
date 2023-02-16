from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import EditProfileForm
from .forms import SignupForm
from django.views.generic import DetailView
from blog.models import Profile


# Registration
class UserRegisterView(generic.CreateView):
    form_class = SignupForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')


# Edit profile
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


# Profile page
class ProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfilePageView, self,).get_context_data(*args, **kwargs)
        user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['user'] = user
        return context


#Edit profile page 
class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'facebook', 'instagram', 'linkedin']
    success_url = reverse_lazy('home')