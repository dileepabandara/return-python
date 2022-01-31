name = input("What is your name? ")
# age = input("How old are you? ")
age = int(input("How old are you? "))

# age_in_dog_years = int(age) * 7;
age_in_dog_years = age * 7;

print("Hello " + name)
print(f"It seems your age {age} is too much old :(")
print(name, age)

print(f"Age in dog year: {age_in_dog_years}")