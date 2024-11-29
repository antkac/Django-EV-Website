from pathlib import Path
import csv
from cars.models import CarMake, CarModel


def run():

    DATA_DIR = Path(__file__).resolve().parent / "data"
    with open(DATA_DIR / "processed_cars_data.csv", 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            make, _ = CarMake.objects.get_or_create(name=row['make'])

            CarModel.objects.create(
                make=make,
                name=row['name'],
                battery=float(row['battery']),
                real_range=int(row['real_range']),
                efficiency=int(row['efficiency']),
                charge_power=float(row['charge_power']),
                drive=row['drive'],
                seats=int(row['seats']),
                tow_hitch=row['tow_hitch'].lower() == 'true',
                top_speed=float(row['top_speed']),
                acceleration=float(row['acceleration']),
                value=int(row['value'])

            )
