import math

UNITS = ["Inches", "Feet", "Centimeters", "Meters", "Yards"]
COMBOS = []


def in_to_feet(inches) -> float:
    feet = inches * 12
    return feet


def in_to_cm(inches) -> float:
    cm = inches * 2.54
    return cm


def in_to_meters(inches) -> float:
    meters = inches / 39.37
    return meters


def in_to_yards(inches) -> float:
    yards = inches / 36
    return yards


def feet_to_inches(feet) -> float:
    inches = feet / 12
    return inches


def feet_to_cm(feet) -> float:
    cm = feet * 30.48
    return cm


def feet_to_meters(feet) -> float:
    meters = feet / 3.281
    return meters


def feet_to_yards(feet) -> float:
    yards = feet / 3
    return yards


def cm_to_in(cm) -> float:
    inches = cm / 2.54
    return inches


def cm_to_feet(cm) -> float:
    feet = cm / 30.48
    return feet


def cm_to_meters(cm) -> float:
    meters = cm / 100
    return meters


def cm_to_yards(cm) -> float:
    yards = cm / 91.44
    return yards


def meters_to_inches(meters) -> float:
    inches = meters * 39.37
    return inches


def meters_to_feet(meters) -> float:
    feet = meters * 3.281
    return feet


def meters_to_cm(meters) -> float:
    cm = meters * 100
    return cm


def meters_to_yards(meters) -> float:
    yards = meters * 1.094
    return yards


def yards_to_inches(yards) -> float:
    inches = yards * 36
    return inches


def yards_to_feet(yards) -> float:
    feet = yards * 3
    return feet


def yards_to_cm(yards) -> float:
    cm = yards * 91.44
    return cm


def yards_to_meters(yards) -> float:
    meters = yards / 1.094
    return meters


def find_combos():
    for i in UNITS:
        for j in UNITS:
            COMBOS.append((i, j))


def check_start_amount(start_amount):
    if type(start_amount) != int or type(start_amount) != float:
        raise ValueError("Starting amount must be either a float or int.")


def check_start_unit(start_unit):
    if type(start_unit) != str:
        raise ValueError("Starting unit must be a string.")


def check_end_unit(end_unit):
    if type(end_unit) != str:
        raise ValueError("Starting unit must be a string.")


def conversion(start_amount, start_unit, end_unit):
    units = (start_unit, end_unit)
    match units:
        # Inches
        case ("Inches", "Feet"):
            in_to_feet(start_amount)
        case ("Inches", "Centimeters"):
            in_to_cm(start_amount)
        case ("Inches", "Meters"):
            in_to_meters(start_amount)
        case ("Inches", "Yards"):
            in_to_yards(start_amount)
        # Feet
        case ("Feet", "Inches"):
            feet_to_inches(start_amount)
        case ("Feet", "Centimeters"):
            feet_to_cm(start_amount)
        case ("Feet", "Yards"):
            feet_to_yards(start_amount)
        case ("Feet", "Meters"):
            feet_to_meters(start_amount)
        # Yards
        case ("Yards", "Centimeters"):
            yards_to_cm(start_amount)
        case ("Yards", "Feet"):
            yards_to_feet(start_amount)
        case ("Yards", "Inches"):
            yards_to_inches(start_amount)
        case ("Yards", "Meters"):
            feet_to_cm(start_amount)
        # Meters
        case ("Meters", "Feet"):
            meters_to_cm(start_amount)
        case ("Meters", "Inches"):
            meters_to_inches
        case ("Meters", "Yards"):
            meters_to_yards
        case ("Meters", "Centimeters"):
            meters_to_cm(start_amount)


def main():

    start_amount = input("Please enter a starting amount as either a float or an int: ")
    check_start_amount(start_amount)

    start_unit = input("Please input a starting unit of measurement: ")
    check_start_unit(start_unit)

    end_unit = input("Please enter the desired unit of measurement to convert to: ")
    check_end_unit(end_unit)

    return conversion(start_amount, start_unit, end_unit)


if __name__ == "__main__":
    main()


print(conversion(int(12), "Inches", "Feet"))
