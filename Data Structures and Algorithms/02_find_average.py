print("*" * 60)
print("Hello student! ")
print("Enter your maths and science marks to find the average")
print("*" * 60)

answer = True
while answer:

    UserMaths = input("Maths marks: ")
    UserScience = input("Science marks: ")
    try:
        maths = int(UserMaths)
        if maths > 100:
            print("Enter valid Maths marks")
            print("*" * 40)
        else:
            science = int(UserScience)
            if science > 100:
                print("Enter valid Science marks")
                print("*" * 40)
            else:
                average = (maths + science) / 2
                averageString = str(average)

                if average >= 75:
                    print("Your total is: ", (maths + science))
                    print("Your average is: " + averageString)
                    print("Your grade is 'A' ")
                    answer = None
                    print("*" * 60)
                if 75 > average >= 65:
                    print("Your total is: ", (maths + science))
                    print("Your average is: " + averageString)
                    print("Your grade is 'B' ")
                    answer = None
                    print("*" * 60)
                if 65 > average >= 55:
                    print("Your total is: ", (maths + science))
                    print("Your average is: " + averageString)
                    print("Your grade is 'C' ")
                    answer = None
                    print("*" * 60)
                if 55 > average >= 30:
                    print("Your total is: ", (maths + science))
                    print("Your average is: " + averageString)
                    print("Your grade is 'D' ")
                    answer = None
                    print("*" * 60)
                if average < 30:
                    print("Your total is: ", (maths + science))
                    print("Your average is: " + averageString)
                    print("Your grade is 'F' ")
                    answer = None
                    print("*" * 60)
    except ValueError:
        print("Oops.. Enter numbers not letters or characters")
        print("*" * 60)
