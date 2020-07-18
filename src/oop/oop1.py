# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Vehicle base class
class Vehicle:
    pass


#Vehicle child class
class GroundVehicle(Vehicle):
    pass

#GroundVehicle child class
class Car(GroundVehicle):
    pass

#GroundVehicle child class
class Motorcycle(GroundVehicle):
    pass




#FlightVehicle base class
class FlightVehicle:
    pass

#FlightVehicle child class
class Airplane(FlightVehicle):
    pass

#Starship base class
class Starship:
    pass


#