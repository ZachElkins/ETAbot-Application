"""
    ETAbot Application Question
    
    Problem:
        Imagine you need to write a program for quickly finding location of things.
    A user would enter information as "dance shoes - basement", "tent - garage", 
    "passport - safe", "beer - fridge", "buckwheat - big pantry". Then the user 
    would want to know where the beer is and use the program to tell. What data 
    structure would you use to store the information and why? Please provide a 
    sample python code of the core functionality and unit testing via github/gitlab 
    or other way.
    
    Solution:
        I decided to use the built in python dictionary structure. There is no need
    for the items to be indexed in this sitaution, so a something like a list would
    be unncessary and not scale well for larger applications.
"""

def main() :
    global items
    items = {"dance shoes": "basement",
            "tent": "garage",
            "passport": "safe",
            "beer": "fridge",
            "buckwheat": "big pantry"}

    exit_program = False;
    while not exit_program :
        exit_program = main_loop()

def print_menu() : 
    print('''
+------------- Menu ------------+
| 1) Input new item             |
| 2) Retrieve location of item  |
| 3) Exit                       |
+ ------------------------------+
    ''')


def input_item() :
    print("What is the name of the item?")
    item = input("> ").lower()
    print("\nWhere is your %s located?" % item)
    location = input("> ").lower()
    
    items[item] = location
    print("\nYour %s is stored in the %s.\n" % (item, location))

def retrieve_item() :

    print("What are you looking for?")

    item_found = False
    while not item_found :
        for item in items :
            print(" - %s" % item)
        print("")
        
        search = input("> ")
        print("")

        if search.lower() == "exit" : 
            return False
        elif search.lower() in items :
            print("\n Your %s can be found in the %s." % (search, items[search]))
            item_found = True
        else :
            print("unknown item `%s`, try again from the list below type `exit`." % search)


def main_loop() :
    print_menu()
    option = input("> ")
    print("")

    if   option == "1" : input_item();    return False
    elif option == "2" : retrieve_item(); return False
    elif option == "3" : return True
    else : print("Invalid command")


if __name__ == "__main__" :
    main()