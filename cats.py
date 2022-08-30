from smtplib import SMTPRecipientsRefused
from unicodedata import name


class AbstractAnimal:
    max_hunger = 50
    greeting = 'Hi!'

    def __init__(self, name, species):
        self.name = name
        self.species = species 

    def speak(self):
        print(f"{self.greeting} I am {self.name} the {self.species}")

    def run(self, animal='This darn pet'):
        print(f'{animal} {self.name} is running after you!!!')

    def has_fur(self):
        print(f'Yep, there\'s definitely fur all over this house.')

class ChasesBallMixin:
    """Likes to chase balls"""
    def chasing_ball(self):
        print(f'Look at that pet chasing that ball, I knew it!')

class Dog(AbstractAnimal, ChasesBallMixin):
    greeting = 'Ruff! Ruff!'
    def __init__(self, name):
        super().__init__(name, "Dog")
    # def speak(self):
    #     super().speak("Ruff ruff!")
    def run(self):
        super().run()

class Cat(AbstractAnimal, ChasesBallMixin):
    """Initialize a cat."""
    species = 'cat'
    max_hunger = 99
    greeting = 'Meow!'

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Cat name={self.name}>'
    
    def purr(self):
        print(f'{self.name} is purring to you.')
    
    # def speak(self):
    #     super().speak("Meow")
    
    def run(self):
        super().run("This darn cat")
    def has_fur(self):
        return super().has_fur()


felix = Cat("Felix")
orion = Cat("Orion")
stella = Dog("Stella")


#add an empty hobby list

#create a method that adds hobby to hobby list

#create a method that takes a nickname

#create a cats list with cats facts

#print hobbies list

#take a cats list and return a dictionary of cats by nickname

#create a function that returns a list of cat objects
