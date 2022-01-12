design = "*"


def basic(typedMobile):
    Name = "Dileepa LBJ"
    age, field = 24, "Computer Science"
    Age = str(age)
    job, yr, country = "Developer", "2021", "Sri Lanka"

    print(design * 40)
    print("PROFILE")
    print(design * 40)
    print("Name: " + Name)
    print("Age: " + Age + " years")
    print("Field: " + field)
    print(job, yr, country)
    print("Mobile no: " + typedMobile)
    print(design * 40)


def two():
    Name = "Dileepa"
    mobile = str(input(Name + " what is your mobile number? \n"))
    mobile2 = "0123456789"

    if mobile == mobile2:
        basic(mobile)
    else:
        print("Wrong number. Cannot access")


two()
