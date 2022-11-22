from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill = 0
    current_taxi = None
    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    option = input(">>> ").lower()
    while option != "q":
        if option == "c":
            current_taxi = get_taxi_choice(current_taxi, taxis)
            print(f"Bill to date: ${bill:.2f}")
            print("q)uit, c)hoose taxi, d)rive")
            option = input(">>> ").lower()

        elif option == "d":
            bill = drive_taxi(bill, current_taxi)
            print(f"Bill to date: ${bill:.2f}")
            print("q)uit, c)hoose taxi, d)rive")
            option = input(">>> ").lower()

        else:
            print("Invalid option")
            print(f"Bill to date: ${bill:.2f}")
            print("q)uit, c)hoose taxi, d)rive")
            option = input(">>> ").lower()

    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def drive_taxi(bill, current_taxi):
    if current_taxi is not None:
        distance = float(input("Drive how far? "))
        current_taxi.drive(distance)
        print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}")
        bill += current_taxi.get_fare()

    else:
        print("You need to choose a taxi before you can drive")
    return bill


def get_taxi_choice(current_taxi, taxis):
    print("Taxis available:")
    display_taxis(taxis)
    try:
        taxi_option = int(input("Choose taxi: "))
        if taxi_option not in range(0, 3):
            print("Invalid taxi choice")
        else:
            current_taxi = taxis[taxi_option]
    except ValueError:
        print("Invalid input")
    return current_taxi


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
