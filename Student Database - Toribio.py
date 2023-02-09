print("**************** PROGRAMMED BY: *****************")
print("************** NHIZALYN TORIBIO ****************")
print("***************** BSCOE 1 -2 *******************")
print("************* FINAL OUTPUT IN DSA **************")


print("\n\t------------- HELLO WELCOME --------------"
      "\n\t======= Database Logs for Students =======")

D = dict()
n = int(input('\n\tNumber of students record you want to store?? '))

# Modification Menu Section
def print_menu():
    print(
        """\n\t
        --------------- DATABASE LOGS ----------------
        \n\t\tWhat would you like to do?
        1. Add Basic Information              [1]
        2. Modify the Information             [2]
        3. Delete Data Information            [3]
        4. View the Entire List Information   [4]
        5. Search an Information              [5]
        6. Exit                               [6]
        """
    )

# This is the List of the Code Containing where the data are stored
Count = 0
print_menu()
Entry_list = []
Firstname_List = []
Lastname_List = []
StudentsAddress_List = []
Marks_List = []
Gender_List = []
Religion_List = []
Age_List = []
Phone_Number = []

while Count <= 1000:
    Choice = input("> What do you wanna do first: ")

    # Add Students Information
    if Choice == "1":
        print("\n>>>>>>>>>>> ADD STUDENT BASIC INFORMATION <<<<<<<<<<<")

        Count = Count + 1
        Entry_list.append(Count)
        print("\n\tStudent Number:", Count)
        Firstname_List.append(input("\tEnter your First Name: "))
        Lastname_List.append(input("\tEnter your Last Name: "))
        Marks_List.append(input("\tEnter your Marks (GWA): "))
        Gender_List.append(input("\tEnter your Gender: "))
        Age_List.append(input("\tEnter your Age: "))
        Religion_List.append(input("\tEnter your Religion: "))
        StudentsAddress_List.append(input("\tEnter your Address Location: "))
        Phone_Number.append(input("\tEnter your Contact Number: "))

        print("\n\tYou have Successfully added a new Student Information.")
        print_menu()

    # The Edit Contact Section
    elif Choice == "2":
        print("\n>>>>>>>>>>> MODIFY INFORMATION <<<<<<<<<<<")

        for Contact in range(len(Entry_list)):
            print("\nSTUDENT NUMBER", Entry_list[Contact])
            print("First name:", Firstname_List[Contact])
            print("Last name:", Lastname_List[Contact])
            print("Mark (GWA):", Marks_List[Contact])
            print("Gender:", Gender_List[Contact])
            print("Age:", Age_List[Contact])
            print("Religion:", Religion_List[Contact])
            print("Address:", StudentsAddress_List[Contact])
            print("Contact number:", Phone_Number[Contact])

        Edit_Contact = int(input("\n> Enter the Students number that you want to edit: "))
        if Edit_Contact in Entry_list:
            index = Entry_list.index(Edit_Contact)
            print("\nSTUDENT NUMBER", Edit_Contact)
            print("First name: ", Firstname_List[index])
            print("Last name: ", Lastname_List[index])
            print("Mark (GWA):", Marks_List[index])
            print("Gender:", Gender_List[index])
            print("Age:", Age_List[index])
            print("Religion:", Religion_List[index])
            print("Address: ", StudentsAddress_List[index])
            print("Contact number:", Phone_Number[index])

            print("\nWhat number would you like to Modify?")
            print("Enter (1) to Change the First name")
            print("Enter (2) to Change the Last name")
            print("Enter (3) to Change the Mark (GWA)")
            print("Enter (4) to Change the Gender")
            print("Enter (5) to Change the Age")
            print("Enter (6) to Change the Religion")
            print("Enter (7) to Change the Address")
            print("Enter (8) to Change the Contact number\n")

            Edit_choice = input("\t> What number do you want to modify: ")

            # This section will change the First name of the Student
            if Edit_choice == "1":
                index = Entry_list.index(Edit_Contact)
                Edit_First = input("Enter New First Name: ")
                Firstname_List[index] = Edit_First
                print("\nSTUDENT NUMBER:", Edit_Contact)
                print("First name:", Firstname_List[index])
                print("Last name:", Lastname_List[index])
                print("Mark (GWA):", Marks_List[index])
                print("Gender:", Gender_List[index])
                print("Age:", Age_List[index])
                print("Religion:", Religion_List[index])
                print("Address:", StudentsAddress_List[index])
                print("Contact number:", Phone_Number[index])
                print("\n<<<<< MODIFICATION COMPLETE >>>>>")

            # This section will change the Last name of the Student
            elif Edit_choice == "2":
                index = Entry_list.index(Edit_Contact)
                Edit_Last = input("Enter New Last Name: ")
                Lastname_List[index] = Edit_Last
                print("\nSTUDENT NUMBER:", Edit_Contact)
                print("First name:", Firstname_List[index])
                print("Last name:", Lastname_List[index])
                print("Mark (GWA):", Marks_List[index])
                print("Gender:", Gender_List[index])
                print("Age:", Age_List[index])
                print("Religion:", Religion_List[index])
                print("Address:", StudentsAddress_List[index])
                print("Contact number:", Phone_Number[index])
                print("\n<<<<< MODIFICATION COMPLETE >>>>>")

            # This section will change the Mark (GWA) of the Student
            elif Edit_choice == "3":
                index = Entry_list.index(Edit_Contact)
                Edit_Marks = input("Enter New Mark (GWA): ")
                Marks_List[index] = Edit_Marks
                print("\nSTUDENT NUMBER:", Edit_Contact)
                print("First name:", Firstname_List[index])
                print("Last name:", Lastname_List[index])
                print("Mark (GWA):", Marks_List[index])
                print("Gender:", Gender_List[index])
                print("Age:", Age_List[index])
                print("Religion:", Religion_List[index])
                print("Address:", StudentsAddress_List[index])
                print("Contact number:", Phone_Number[index])
                print("\n<<<<< MODIFICATION COMPLETE >>>>>")

            # This section will change the Gender of the Student
            elif Edit_choice == "4":
                index = Entry_list.index(Edit_Contact)
                Edit_Gender = input("Enter New Gender: ")
                Gender_List[index] = Edit_Gender
                print("\nSTUDENT NUMBER:", Edit_Contact)
                print("First name:", Firstname_List[index])
                print("Last name:", Lastname_List[index])
                print("Mark (GWA):", Marks_List[index])
                print("Gender:", Gender_List[index])
                print("Age:", Age_List[index])
                print("Religion:", Religion_List[index])
                print("Address:", StudentsAddress_List[index])
                print("Contact number:", Phone_Number[index])
                print("\n<<<<< MODIFICATION COMPLETE >>>>>")

            # This section will change the Age of the Student
            elif Edit_choice == "5":
                index = Entry_list.index(Edit_Contact)
                Edit_Age = input("Enter New Age: ")
                Age_List[index] = Edit_Age
                print("\nSTUDENT NUMBER:", Edit_Contact)
                print("First name:", Firstname_List[index])
                print("Last name:", Lastname_List[index])
                print("Mark (GWA):", Marks_List[index])
                print("Gender:", Gender_List[index])
                print("Age:", Age_List[index])
                print("Religion:", Religion_List[index])
                print("Address:", StudentsAddress_List[index])
                print("Contact number:", Phone_Number[index])
                print("\n<<<<< MODIFICATION COMPLETE >>>>>")

            # This section will change the Religion of the Student
            elif Edit_choice == "6":
                index = Entry_list.index(Edit_Contact)
                Edit_Religion = input("Enter New Religion: ")
                Religion_List[index] = Edit_Religion
                print("\nSTUDENT NUMBER:", Edit_Contact)
                print("First name:", Firstname_List[index])
                print("Last name:", Lastname_List[index])
                print("Mark (GWA):", Marks_List[index])
                print("Gender:", Gender_List[index])
                print("Age:", Age_List[index])
                print("Religion:", Religion_List[index])
                print("Address:", StudentsAddress_List[index])
                print("Contact number:", Phone_Number[index])
                print("\n<<<<< MODIFICATION COMPLETE >>>>>")

            # This section will change the Address of the Student
            elif Edit_choice == "7":
                index = Entry_list.index(Edit_Contact)
                Edit_address = input("Enter New Address: ")
                StudentsAddress_List[index] = Edit_address
                print("\nSTUDENT NUMBER:", Edit_Contact)
                print("First name:", Firstname_List[index])
                print("Last name:", Lastname_List[index])
                print("Mark (GWA):", Marks_List[index])
                print("Gender:", Gender_List[index])
                print("Age:", Age_List[index])
                print("Religion:", Religion_List[index])
                print("Address:", StudentsAddress_List[index])
                print("Contact number:", Phone_Number[index])
                print("\n<<<<< MODIFICATION COMPLETE >>>>>")

            # This section will change the Phone Number of the Student
            elif Edit_choice == "8":
                index = Entry_list.index(Edit_Contact)
                Edit_Phone_number = input("Enter New Phone number: ")
                Phone_Number[index] = Edit_Phone_number
                print("\nSTUDENT NUMBER:", Edit_Contact)
                print("First name:", Firstname_List[index])
                print("Last name:", Lastname_List[index])
                print("Mark (GWA):", Marks_List[index])
                print("Gender:", Gender_List[index])
                print("Age:", Age_List[index])
                print("Religion:", Religion_List[index])
                print("Address:", StudentsAddress_List[index])
                print("Contact number:", Phone_Number[index])
                print("\n<<<<< MODIFICATION COMPLETE >>>>>")
            else:
                print("The Student Number does not exist!")
        else:
            print("The Student Number does not exist!")
        print_menu()

    # The Delete Contact Section:
    elif Choice == "3":
        print("\n>>>>>>>>>>> DELETE DATA INFORMATION <<<<<<<<<<<")

        Entry_Number = int(input("\nEnter the Student Number that you want to delete in the Database: "))
        if Entry_Number in Entry_list:
            index = Entry_list.index(Entry_Number)
            print("\nThe Student number", Entry_Number)
            Entry_list.pop()
            print("First name:", Firstname_List.pop(index))
            print("Last name:", Lastname_List.pop(index))
            print("Mark (GWA):", Marks_List.pop[index])
            print("Gender:", Gender_List.pop[index])
            print("Age:", Age_List.pop[index])
            print("Religion:", Religion_List.pop[index])
            print("Address:", StudentsAddress_List.pop(index))
            print("Contact number:", Phone_Number.pop(index))
            print("\n<<<<< This Student Number Data has been Deleted >>>>>")
            print("<<<<<<<<<<< DELETE COMPLETE >>>>>>>>>>>>")
            Count -= 1
        else:
            print("\nThe Student number does not exist.")
        print_menu()
