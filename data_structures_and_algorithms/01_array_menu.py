from pip._vendor.distlib.compat import raw_input

print()
print("*" * 62)
print("""\tHi I'm Dileepa. Welcome to my array menu program""")
print("*" * 62 + "\n")

answer = True
while answer:
    try:
        num_array = list()
        num = raw_input("How many elements you want to your array? ")
        for i in range(int(num)):
            n = raw_input("#Enter a number : ")
            num_array.append(int(n))
        print("\nArray created successfully!")

        ans = True
        while ans:
            print("*" * 60)
            print("""
            Array Menu
            Your array: """, num_array)
            print("""
            1.Add a number
            2.Sort in ascending order
            3.Sort in descending order
            4.Search index of a number
            5.Delete a number
            6.Update a number
            7.Exit
            """)
            ans = input("What would you like to do? ")

            if ans == "1":
                try:
                    indexAddValue = int(input("Enter number to add: "))
                    indexAddIndex = len(num_array) + 1
                    num_array.insert(indexAddIndex, indexAddValue)
                    print(indexAddValue, " successfully added!")
                except ValueError:
                    print("Oops.. Enter valid input")

            elif ans == "2":
                num_array.sort()
                print("Ascending order: ", num_array)
                print("Array successfully sorted in ascending order!")

            elif ans == "3":
                num_array.sort(reverse=True)
                print("Descending order: ", num_array)
                print("Array successfully sorted in descending order!")

            elif ans == "4":
                try:
                    serNum = int(input("Enter number to search: "))
                    print("Array index for ", serNum, " is ", num_array.index(serNum))
                except ValueError:
                    print("Oops.. Enter valid input")

            elif ans == "5":
                try:
                    delNum = int(input("Enter number to delete: "))
                    num_array.remove(delNum)
                    print(delNum, " successfully deleted!")
                except ValueError:
                    print("Oops.. Enter valid input")

            elif ans == "6":
                try:
                    updNumIndex = int(input("Enter number index to update: "))
                    updNumValue = int(input("Enter update value: "))
                    num_array[updNumIndex] = updNumValue
                    print("Array successfully updated!")
                except ValueError:
                    print("Oops.. Enter valid input")

            elif ans == "7":
                print("\n Thanks. Have a nice day!")
                ans = None
                answer = None

            else:
                print("\n Oops.. :( not valid choice try again ;)")
    except ValueError:
        print("Oops.. only numbers are allowed. Please enter numbers\n")
