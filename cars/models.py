from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class CarMake(models.Model):
    name = models.CharField(max_length=40, unique=True, default="Other")  # Enforce unique car makes

    def __str__(self):
        return self.name


''' NOT IMPLEMENTED
def car_model_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / CarModel_<id>/<filename> 
    return "images/"+"CarModel_{0}/{1}".format(instance.CarModel.id, filename)
'''


class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name="models")
    name = models.CharField(max_length=100)
    acceleration = models.FloatField(help_text="Acceleration in seconds (0-100 km/h)")
    top_speed = models.FloatField(help_text="Top speed in km/h")
    drive = models.CharField(max_length=20, help_text="e.g., RWD, FWD, AWD")
    battery = models.FloatField(help_text="Usable battery capacity in kWh")
    charge_power = models.FloatField(help_text="Maximum charge power in kW")
    real_range = models.IntegerField(help_text="Real-world range in km")
    efficiency = models.IntegerField(help_text="Efficiency in Wh/km")
    seats = models.IntegerField(validators=[MinValueValidator(1)], help_text="Number of seats")
    tow_hitch = models.BooleanField(default=False, help_text="Tow hitch available?")
    value = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))]
    )
    image = models.ImageField(upload_to='images/', default="images/sample.jpg", null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['make', 'name'], name='unique_car_model_per_make')
        ]

    def __str__(self):
        return f"{self.make.name} {self.name}"


class Car(models.Model):
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name="cars")
    year = models.IntegerField()
    rate = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))]
    )
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.model.name} ({self.year})"


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Rental(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="rentals")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="rentals")
    start_date = models.DateField()
    end_date = models.DateField()
    total_cost = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))]
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Rental {self.car} by {self.customer} ({self.start_date} to {self.end_date})"
