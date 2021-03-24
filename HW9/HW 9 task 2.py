from time import sleep


class BatteryLow(Exception):
    pass


class BatteryDischarge(Exception):
    pass


class FullContainer(Exception):
    pass


class NoWater(Exception):
    pass


class RobotVacuumCleaner:
    name = "Connor"
    battery_use = 5
    water_use = 10
    garbage_fill = 10

    def __init__(self):
        self.battery = 100
        self.garbage = 0
        self.water = 100

    def move(self):
        print(f"{self.name} wakes up")
        while True:
            sleep(1)
            try:
                print("Moving")
                self.battery -= self.battery_use
                if self.battery <= 20:
                    if self.battery == 0:
                        raise BatteryDischarge
                    raise BatteryLow
            except BatteryLow:
                print(f"Warning: battery is only {self.battery}% left.")
            except BatteryDischarge:
                print("Battery discharged. Take me to the station.")
                break

            try:
                print(f"{self.name} is working")
                self.vacuum_cleaner()
                if self.garbage == 100:
                    raise FullContainer
            except FullContainer:
                print("Garbage container is full")
                input("Press enter to empty the container")
                print()
                self.garbage = 0

            try:
                if self.water > 0:
                    print(f"{self.name} is washing")
                    self.wash()
                else:
                    raise NoWater
            except NoWater:
                print("Run out of water. Please refill water tank.")

    def wash(self):
        self.water -= self.water_use
        print(f"Washing... {self.water} water level")

    def vacuum_cleaner(self):
        self.garbage += self.garbage_fill
        print(f"Vacuum cleaning... {self.garbage} garbage level")


robot = RobotVacuumCleaner()
robot.move()