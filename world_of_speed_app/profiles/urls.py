from django.urls import path

from world_of_speed_app.profiles.views import create_profile, ProfileDetail, ProfileEdit, DeleteProfileView

urlpatterns = (
    path('create/', create_profile, name="create_profile"),
    path('details', ProfileDetail.as_view(), name="details_profile"),
    path('edit/', ProfileEdit.as_view(), name="edit_profile"),
    path('delete/', DeleteProfileView.as_view(), name="delete_profile"),
)