def add_employee(data):
    emp_id = int(input("Enter your id: "))
    name = input("Enter your name: ")

    data[emp_id] = name
    print("Employee Data Added")

def view_employee(data):
    if not data:
        print("no record found")
        return

    for emp_id , name in data.items():
        print(emp_id , ":" , name)

def delete_employee(data):
    emp_id = int(input("Enter Id you want to delete: "))

    if emp_id in data:
        confirm = input("ARE YOU SURE (yes/no): ")
        if confirm.lower() == "yes":
            del data[emp_id]
            print("Deleted employee successfully")
        else:
            print("okay not deleted")
    else:
        print("Employee not found")
       
def main():
    data = {}

    while True:
        print("1. ADD EMPLOYEE")
        print("2. VIEW EMPLOYEE")
        print("3. DELETE EMPLOYEE")
        print("4. EXIT")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_employee(data)
        elif choice == 2:
            view_employee(data)
        elif choice == 3:
            delete_employee(data)
        elif choice == 4:
            print("BYE BYE")
            break
        else:
            print("INVALID CHOICE")

main()

