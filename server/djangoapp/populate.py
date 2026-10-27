from .models import CarMake, CarModel

CARS = [
    {
        "name": "NISSAN",
        "description": "Great cars. Japanese technology",
        "country": "Japan",
        "models": [
            ("Pathfinder", "SUV", 2023),
            ("Qashqai", "SUV", 2023),
            ("XTRAIL", "SUV", 2023),
        ],
    },
    {
        "name": "Mercedes",
        "description": "Great cars. German technology",
        "country": "Germany",
        "models": [
            ("A-Class", "SUV", 2023),
            ("C-Class", "SUV", 2023),
            ("E-Class", "SUV", 2023),
        ],
    },
    {
        "name": "Audi",
        "description": "Great cars. German technology",
        "country": "Germany",
        "models": [
            ("A4", "SEDAN", 2023),
            ("A6", "SEDAN", 2023),
            ("Q5", "SUV", 2022),
        ],
    },
    {
        "name": "Kia",
        "description": "Great cars. Korean technology",
        "country": "South Korea",
        "models": [
            ("Sorrento", "SUV", 2023),
            ("Carnival", "SUV", 2023),
            ("Cerato", "SEDAN", 2023),
        ],
    },
    {
        "name": "Toyota",
        "description": "Great cars. Japanese technology",
        "country": "Japan",
        "models": [
            ("Camry", "SEDAN", 2023),
            ("Corolla", "SEDAN", 2023),
            ("Land Cruiser", "SUV", 2023),
        ],
    },
]


def initiate():
    """Create the sample car makes and models if they do not exist yet."""
    for car in CARS:
        make, _ = CarMake.objects.get_or_create(
            name=car["name"],
            defaults={
                "description": car["description"],
                "country": car["country"],
            },
        )
        for name, car_type, year in car["models"]:
            CarModel.objects.get_or_create(
                car_make=make,
                name=name,
                defaults={"type": car_type, "year": year},
            )
