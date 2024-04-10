from django.urls import path

from world_of_speed_app.cars.views import CatalogueCar, CreateCar, DetailCar, EditCar, DeleteCar

urlpatterns = (
    path("catalogue/", CatalogueCar.as_view(), name="catalogue"),
    path("create/", CreateCar.as_view(), name="create_car"),
    path("<int:pk>/details", DetailCar.as_view(), name="details_car"),
    path("<int:pk>/edit", EditCar.as_view(), name="edit_car"),
    path("<int:pk>/delete", DeleteCar.as_view(), name="delete_car"),
)