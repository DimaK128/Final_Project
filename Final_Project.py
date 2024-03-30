# Define some example of car data
cars = [
    {"model": "Toyota Camry", "year": 2022, "price": 25000, "type": "Sedan"},
    {"model": "Honda Accord", "year": 2023, "price": 24000, "type": "Sedan"},
    {"model": "Hyundai Sonata", "year": 2020, "price": 23000, "type": "Sedan"},
    {"model": "Kia Optima", "year": 2019, "price": 21000, "type": "Sedan"},
    {"model": "Chevrolet Malibu", "year": 2018, "price": 20000, "type": "Sedan"},
    {"model": "Ford Fusion", "year": 2017, "price": 19000, "type": "Sedan"},

    {"model": "Ford Escape", "year": 2024, "price": 26000, "type": "SUV"},
    {"model": "Toyota RAV4", "year": 2023, "price": 28000, "type": "SUV"},
    {"model": "Honda CR-V", "year": 2022, "price": 27000, "type": "SUV"},
    {"model": "Jeep Wrangler", "year": 2021, "price": 29000, "type": "SUV"},
    {"model": "Subaru Forester", "year": 2020, "price": 25000, "type": "SUV"},
    {"model": "Nissan Rogue", "year": 2019, "price": 22000, "type": "SUV"},
    {"model": "Hyundai Tucson", "year": 2018, "price": 23000, "type": "SUV"},

    {"model": "Chevrolet Silverado", "year": 2024, "price": 35000, "type": "Truck"},
    {"model": "Ford F-150", "year": 2023, "price": 37000, "type": "Truck"},
    {"model": "Ram 1500", "year": 2022, "price": 33000, "type": "Truck"},
    {"model": "Toyota Tundra", "year": 2021, "price": 32000, "type": "Truck"},
    {"model": "Nissan Titan", "year": 2020, "price": 30000, "type": "Truck"},
    {"model": "GMC Sierra", "year": 2019, "price": 34000, "type": "Truck"},

    {"model": "Toyota Prius", "year": 2024, "price": 28000, "type": "Hatchback"},
    {"model": "Honda Civic", "year": 2023, "price": 22000, "type": "Hatchback"},
    {"model": "Mazda 3", "year": 2022, "price": 25000, "type": "Hatchback"},
    {"model": "Volkswagen Golf", "year": 2020, "price": 23000, "type": "Hatchback"},
    {"model": "Subaru Impreza", "year": 2019, "price": 18000, "type": "Hatchback"},
    {"model": "Ford Focus", "year": 2018, "price": 19000, "type": "Hatchback"},

    {"model": "Ford Mustang", "year": 2024, "price": 38000, "type": "Coupe"},
    {"model": "Chevrolet Camaro", "year": 2024, "price": 37000, "type": "Coupe"},
    {"model": "Dodge Challenger", "year": 2023, "price": 39000, "type": "Coupe"},
    {"model": "Nissan Z", "year": 2022, "price": 35000, "type": "Coupe"},
    {"model": "Subaru BRZ", "year": 2020, "price": 28000, "type": "Coupe"},
    {"model": "Ford Mustang", "year": 2016, "price": 34000, "type": "Coupe"},
]


# Function to filter cars based on criteria
def filter_cars(cars, budget, year, car_type):
    filtered_cars = []
    for car in cars:
        if (car["price"] <= budget) and (car["year"] >= year):
            if car_type == "all" or car["type"].lower() == car_type.lower():
                filtered_cars.append(car)
    return filtered_cars


# Get user input with validation
def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_valid_year(prompt):
    while True:
        try:
            year = int(input(prompt))
            if year < 2016:
                print("Year must be 2016 or later.")
            else:
                return year
        except ValueError:
            print("Invalid input. Please enter a year.")


def get_car_type(prompt):
    valid_types = ["sedan", "suv", "truck", "hatchback", "coupe", "all"]
    while True:
        car_type = input(prompt).lower()
        if car_type in valid_types:
            return car_type
        else:
            print(f"Invalid car type. Please choose from: {', '.join(valid_types)}")


# Get user input
budget = get_valid_float("Enter your budget in USD: $ ")
year = get_valid_year("What year or newer (e.g., 2020): ")
car_type = get_car_type("Enter preferred car type (Sedan, SUV, Truck, Hatchback, Coupe, or all): ")

# Filter cars based on user input
filtered_cars = filter_cars(cars, budget, year, car_type)

# Display results to user
if filtered_cars:
    print("Great choices! Here are some cars that match your criteria:")
    for car in filtered_cars:
        print(f"{car['year']} {car['model']} ({car['type']}) - ${car['price']:,.2f}")
else:
    print("No cars found matching your criteria. Try adjusting your budget or year.")
