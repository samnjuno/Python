class Smartphone:
    def __init__(self, brand, model, battery_percentage, os_version):
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage
        self.os_version = os_version
    
    def make_call(self, number):
        print(f"Calling {number}... 📞")
    
    def send_text(self, number, message):
        print(f"Sending text to {number}: {message} 📱")
    
    def check_battery(self):
        print(f"Battery is at {self.battery_percentage}% 🔋")
    
    def upgrade_os(self):
        print(f"Upgrading {self.model} to OS version {self.os_version + 1} 📲")
        self.os_version += 1

# Creating a Smartphone object
iphone = Smartphone("Apple", "iPhone 15", 85, 16)

# Using the methods
iphone.make_call("123-456-7890")
iphone.send_text("123-456-7890", "Hey, how are you?")
iphone.check_battery()
iphone.upgrade_os()


# polymorphism
class Vehicle:
    def move(self):
        pass  # This will be overridden by subclasses

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Bike(Vehicle):
    def move(self):
        print("Riding 🚲")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Creating objects of different vehicles
car = Car()
bike = Bike()
plane = Plane()

# Demonstrating polymorphism
vehicles = [car, bike, plane]
for vehicle in vehicles:
    vehicle.move()  # Each vehicle will call its own move() method
