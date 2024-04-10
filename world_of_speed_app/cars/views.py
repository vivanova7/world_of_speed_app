from django.forms import modelform_factory

from django.urls import reverse_lazy
from django.views import generic as views

from world_of_speed_app.cars.forms import CarForm
from world_of_speed_app.cars.models import Car


class ReadonlyMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        for field in form.fields.values():
            field.widget.attrs['readonly'] = 'readonly'

        return form
class CatalogueCar(views.ListView):
    queryset = Car.objects.all()
    template_name = 'cars/catalogue.html'

class CreateCar(views.CreateView):
    queryset = Car.objects.all()
    form_class = CarForm
    template_name = 'cars/car-create.html'
    success_url = reverse_lazy("catalogue")

class DetailCar(views.DetailView):
    queryset = Car.objects.all()
    template_name = 'cars/car-details.html'

class EditCar(views.UpdateView):
    queryset = Car.objects.all()
    form_class = CarForm
    template_name = 'cars/car-edit.html'
    success_url = reverse_lazy("catalogue")

class DeleteCar(views.DeleteView, ReadonlyMixin):
    queryset = Car.objects.all()
    template_name = 'cars/car-delete.html'
    success_url = reverse_lazy("catalogue")

    form_class = modelform_factory(
        Car,
        fields=(
            'type', 'model', 'year', 'image_url', 'price',
        )
    )

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs