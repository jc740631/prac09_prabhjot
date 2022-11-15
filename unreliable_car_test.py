from unreliable_car import UnreliableCar


good_car = UnreliableCar("Brand new", 100, 95)
ok_car = UnreliableCar("3-year car", 100, 60)
bad_car = UnreliableCar("20-year car", 100, 10)

# test drive()
for i in range(5):
    print(f"{good_car.name} did drive {good_car.drive(10)}km")
    print(f"{ok_car.name} did drive {ok_car.drive(10)}km")
    print(f"{bad_car.name} did drive {bad_car.drive(10)}km")

# test __str__
print(good_car)
print(ok_car)
print(bad_car)
