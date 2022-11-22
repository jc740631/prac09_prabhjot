from prac_08.silver_service_taxi import SilverServiceTaxi


my_taxi = SilverServiceTaxi("myTaxi", 100, 2)
my_taxi.drive(18)
print(f"Expected fare: 48.78. Got {my_taxi.get_fare()}")
print(my_taxi)