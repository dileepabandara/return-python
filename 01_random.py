import random

language = [
    "Python",
    "Java",
    "JavaScript",
    "Dart",
    "C",
    "Ruby",
]

people = [
    "Spider-Man",
    "Batman",
    "Superman",
    "Captain America",
    "Iron Man",
    "Thor",
]

random_language = random.choice(language)
random_people = random.choice(people)

print(random_people +  ' likes ' + random_language)