from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from world_of_speed_app.profiles.forms import ProfileForm, ProfileEditForm
from world_of_speed_app.profiles.models import Profile
from world_of_speed_app.utils.profile_helpers import get_profile


# Create your views here.
def create_profile(request):
    form = ProfileForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        "form": form,
        "no_nav": True,
    }
    return render(request, 'profiles/profile-create.html', context)

class ProfileDetail(views.DetailView):
    queryset = Profile.objects.all()
    template_name = 'profiles/profile-details.html'

    def get_object(self, queryset=None):
        return get_profile()

class ProfileEdit(views.UpdateView):
    queryset = Profile.objects.all()
    template_name = 'profiles/profile-edit.html'
    form_class = ProfileEditForm
    success_url = reverse_lazy('details_profile')

    def get_object(self, queryset=None):
        return get_profile()


class DeleteProfileView(views.DeleteView):
    template_name = "profiles/profile-delete.html"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return get_profile()

