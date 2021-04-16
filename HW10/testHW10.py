import unittest

from HW10 import RobotVacuumCleaner


class TestRobotVacuumCleaner(unittest.TestCase):

        
    def test_init(self):
        self.robot = RobotVacuumCleaner(100, 0, 100)
        self.robot1 = RobotVacuumCleaner("100", 0, 25)
        self.robot2 = RobotVacuumCleaner(-20, 75, 0)
        self.robots = [self.robot, self.robot1, self.robot2]
        with self.assertRaises(ValueError):
            RobotVacuumCleaner("grr", 15, 15)

        for item in self.robots:
            self.assertIsInstance(item.battery, int)
            self.assertIsInstance(item.garbage, int)
            self.assertIsInstance(item.water, int)

    def test_move(self):
        self.assertNotEqual(RobotVacuumCleaner.battery_use, 0)
        self.values1 = RobotVacuumCleaner(0, 100, 0)
        self.values1.move()
        self.values2 = RobotVacuumCleaner(100, 0, 100)
        self.values2.cleaning_time = 10
        self.values2.move()

    def test_wash(self):
        self.assertNotEqual(RobotVacuumCleaner.water_use, 0)

    def test_vacuum_cleaner(self):
        self.assertNotEqual(RobotVacuumCleaner.garbage_fill, 0)

    def tearDown(self) -> None:
        print("tearDown")
