employee_data = [
    {"Employee ID": "161E90", "Name": "Raman", "Age": 41, "Salary (PM)": 56000},
    {"Employee ID": "161F91", "Name": "Himadri", "Age": 38, "Salary (PM)": 67500},
    {"Employee ID": "161F99", "Name": "Jaya", "Age": 51, "Salary (PM)": 82100},
    {"Employee ID": "171E20", "Name": "Tejas", "Age": 30, "Salary (PM)": 55000},
    {"Employee ID": "171G30", "Name": "Ajay", "Age": 45, "Salary (PM)": 44000}
]

def search_employee_data():
    print("Search Options:")
    print("1. Age")
    print("2. Name")
    print("3. Salary (>, <, <=, >=)")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        age = int(input("Enter age to search: "))
        result = [employee for employee in employee_data if employee["Age"] == age]
    elif choice == "2":
        name = input("Enter name to search: ")
        result = [employee for employee in employee_data if employee["Name"].lower() == name.lower()]
    elif choice == "3":
        salary_condition = input("Enter salary condition (>, <, <=, >=): ")
        salary_value = int(input("Enter salary value: "))
        
        if salary_condition == ">":
            result = [employee for employee in employee_data if employee["Salary (PM)"] > salary_value]
        elif salary_condition == "<":
            result = [employee for employee in employee_data if employee["Salary (PM)"] < salary_value]
        elif salary_condition == ">=":
            result = [employee for employee in employee_data if employee["Salary (PM)"] >= salary_value]
        elif salary_condition == "<=":
            result = [employee for employee in employee_data if employee["Salary (PM)"] <= salary_value]
        else:
            print("Invalid salary condition.")
            return
    else:
        print("Invalid choice.")
        return

    if not result:
        print("No matching records found.")
    else:
        print("Matching Records:")
        for employee in result:
            print(f"Employee ID: {employee['Employee ID']}, Name: {employee['Name']}, Age: {employee['Age']}, Salary (PM): {employee['Salary (PM)']}")

while True:
    print("\nEmployee Table:")
    print("Employee ID   Name       Age   Salary (PM)")
    for employee in employee_data:
        print(f"{employee['Employee ID']}    {employee['Name']}    {employee['Age']}    {employee['Salary (PM)']}")
    
    search_employee_data()
    
    cont = input("Do you want to search again? (yes/no): ")
    if cont.lower() != "yes":
        break