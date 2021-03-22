from __future__ import annotations

from typing import Dict, Any

from abc import ABC, abstractmethod

import random

import uuid

import time


class Animal(ABC):

    def __init__(self, power: int, speed: int):
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self, forest: Forest):
        raise NotImplementedError('Your method is not implemented')


class Predator(Animal):

    def eat(self, forest: Forest):
        prey = random.choice(list(forest.animals.values()))
        if prey.id == self.id:
            print("No prey found, predator left without dinner")
        else:
            print(f"{__class__.__name__} with {self.current_power} power and {self.speed} speed "
                  f"starts hunting for prey {prey.__class__.__name__} with {prey.current_power} power and {prey.speed} speed")
            if self.speed > prey.speed:
                print("Predator caught the prey")
                if self.current_power > prey.current_power:
                    print("Predator won and eats the prey")
                    won_battle(self, prey)
                    power_recovery(self)

                else:
                    print("Predator lost in battle")
                    lost_battle(self)
                    lost_battle(prey)

            else:
                print("The prey ran away")
                failed_chase(self)
                failed_chase(prey)


class Herbivorous(Animal):

    def eat(self, forest: Forest):
        power_recovery(self)


def power_recovery(animal: AnyAnimal):
    print(f"{animal.__class__.__name__} is eating with {animal.current_power} power")
    if animal.current_power + animal.max_power * 0.5 >= animal.max_power:
        animal.current_power = animal.max_power
    else:
        animal.current_power = round(animal.current_power + animal.max_power * 0.5, 1)
    print(f"{animal.__class__.__name__} ate and recovered power to {animal.current_power}")


def won_battle(predator: AnyAnimal, herbivorous: AnyAnimal):
    if herbivorous.current_power - predator.current_power <= 0:
        forest.remove_animal(herbivorous)
        print(f"{herbivorous.__class__.__name__} died in a battle")
    else:
        herbivorous.current_power -= predator.current_power
        print(f"{herbivorous.__class__.__name__} survived with {herbivorous.current_power}")


def lost_battle(animal: AnyAnimal):
    if animal.current_power - animal.max_power * 0.3 <= 0:
        forest.remove_animal(animal)
        print(f"{animal.__class__.__name__} died in a battle")

    else:
        animal.current_power = round(animal.current_power - animal.max_power * 0.3, 1)
        print(f"{animal.__class__.__name__} lost battle with {animal.current_power} power left")


def failed_chase(animal: AnyAnimal):
    if animal.current_power - animal.max_power * 0.3 <= 0:
        forest.remove_animal(animal)
        print(f"{animal.__class__.__name__} died in a battle")

    else:
        animal.current_power = round(animal.current_power - animal.max_power * 0.3, 1)
        print(f"{animal.__class__.__name__} has {animal.current_power} power left after failed chase")


AnyAnimal: Any[Herbivorous, Predator]


class Forest:

    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        print(f"New animal added to the forest", animal)
        self.animals.update({animal.id: animal})

    def remove_animal(self, animal: AnyAnimal):
        print(f"{animal.__class__.__name__} removed from the forest")
        self.animals.pop(animal.id)

    def any_predator_left(self):
        for x in list(self.animals.values()):
            if x.__class__.__name__ == "Predator":
                print(f"{x.__class__.__name__} is in the forest")
                return True
            print(f"Only {x.__class__.__name__} live in the forest")
            return False


def animal_generator():
    while True:
        new_animal = random.choice((Herbivorous(random.randrange(25, 100, 1), random.randrange(25, 100, 1)),
                                    Predator(random.randrange(25, 100, 1), random.randrange(25, 100, 1))))
        new_animal.id = uuid.uuid4()
        yield new_animal


if __name__ == "__main__":
    forest = Forest()
    nature = animal_generator()

    for i in range(10):
        animal = next(nature)
        print(animal.__dict__)
        forest.add_animal(animal)
    print([{x.__class__.__name__: x.__dict__} for x in list(forest.animals.values())])

    while True:
        if not forest.any_predator_left():
            break
        random.choice(list(forest.animals.values())).eat(forest)
        print([{x.__class__.__name__: x.__dict__} for x in list(forest.animals.values())])
        time.sleep(1)