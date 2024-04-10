from world_of_speed_app.cars.models import Car
from world_of_speed_app.profiles.models import Profile


def get_profile():
    return Profile.objects.first()

def get_cars():
    return Car.objects.all()