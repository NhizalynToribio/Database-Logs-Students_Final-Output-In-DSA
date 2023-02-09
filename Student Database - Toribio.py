print("**************** PROGRAMMED BY: *****************")
print("************** NHIZALYN TORIBIO ****************")
print("***************** BSCOE 1 -2 *******************")
print("************* FINAL OUTPUT IN DSA **************")


print("\n\t------------- HELLO WELCOME --------------"
      "\n\t========= Students Database Logs =========")

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

Count = 0
print_menu()
Entry_list = []
Firstname_List = []
Lastname_List = []
StudentsAddress_List = []
Marks_List = []
Gender_List = []
Phone_Number = []
Religion_List = []
Age_List = []

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
        Marks_List.append(input("\tEnter your Mark: "))
        Gender_List.append(input("\tEnter your Gender: "))
        Age_List.append(input("\tEnter your Age: "))
        Religion_List.append(input("Enter your Religion: "))
        StudentsAddress_List.append(input("\tEnter your Address Location: "))
        Phone_Number.append(input("\tEnter your Contact Number: "))

        print("\n\tYou have Successfully added a new Entry of contact.")
        print_menu()

# Add student information to the dictionary
for i in range(0, n):
    x, y = input("Enter the complete name (First and last name) of student: ").split()
    z = input("Enter contact number: ")
    m = input('Enter Marks: ')
    D[x, y] = (z, m)


# define a function for shorting
# names based on first name
def sort():
    ls = list()
    # fetch key and value using
    # items() method
    for sname, details in D.items():
        # store key parts as an tuple
        tup = (sname[0], sname[1])

        # add tuple to the list
        ls.append(tup)

        # sort the final list of tuples
    ls = sorted(ls)
    for i in ls:
        # print first name and second name
        print(i[0], i[1])
    return


# define a function for
# finding the minimum marks
# in stored data
def minmarks():
    ls = list()
    # fetch key and value using
    # items() methods
    for sname, details in D.items():
        # add details second element
        # (marks) to the list
        ls.append(details[1])

        # sort the list elements
    ls = sorted(ls)
    print("Minimum marks: ", min(ls))

    return


# define a function for searching
# student contact number
def searchdetail(fname):
    ls = list()

    for sname, details in D.items():
        tup = (sname, details)
        ls.append(tup)

    for i in ls:
        if i[0][0] == fname:
            print(i[1][0])
    return


# define a function for
# asking the options
def option():
    choice = int(input('Enter the operation detail: \n \
    1: Sorting using first name \n \
    2: Finding Minimum marks \n \
    3: Search contact number using first name: \n \
    4: Exit\n \
    Option: '))

    if choice == 1:
        # function call
        sort()
        print('Want to perform some other operation??? Y or N: ')
        inp = input()
        if inp == 'Y':
            option()

        # exit function call
        exit()

    elif choice == 2:
        minmarks()
        print('Want to perform some other operation??? Y or N: ')

        inp = input()
        if inp == 'Y':
            option()
        exit()

    elif choice == 3:
        first = input('Enter first name of student: ')
        searchdetail(first)

        print('Want to perform some other operation??? Y or N: ')
        inp = input()
        if inp == 'Y':
            option()

        exit()
    else:
        print('Thanks for executing me!!!!')
        exit()


option()
