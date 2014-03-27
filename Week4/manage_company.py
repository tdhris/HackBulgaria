import sqlite3


def list_employees(cursor):
    result = cursor.execute("SELECT name, position FROM company")
    for row in result:
        name = row[0]
        position = row[1]
        print(name, ' - ', position)


def get_monthly_spending(cursor):
    salaries = cursor.execute("SELECT monthly_salary FROM company")
    monthly_spending = 0
    for salary in salaries:
        monthly_spending += int(salary[0])
    return monthly_spending


def get_yearly_spending(cursor):
    spendings_per_month = cursor.execute("SELECT monthly_salary, yearly_bonus FROM company")
    yearly_spending = 0
    months = 12
    for row in spendings_per_month:
        yearly_spending += int(row[0]) * months
        yearly_spending += int(row[1])
    return yearly_spending


def add_employee(cursor):
    cursor.execute("SELECT employee_id FROM company")
    employee_id = len(cursor.fetchall()) + 1
    name = input("Enter name> ")
    monthly_salary = input("Enter monthly salary> ")
    yearly_bonus = input("Enter yearly bonus> ")
    position = input("Enter position> ")
    cursor.execute("INSERT INTO company VALUES (?, ?, ?, ?, ?)", (employee_id, name, monthly_salary, yearly_bonus, position))


def delete_employee(cursor, unfortunate_id):
    cursor.execute("DELETE FROM company WHERE employee_id = ?", (int(unfortunate_id), ))


def update_employee(cursor, employee_id):
    what_to_update = input("What do you want to update (name, monthly_salary, yearly_bonus or position? > ")
    update = input("What is the new {0} ? > ".format(what_to_update))
    cursor.execute("UPDATE company SET {0} = ? WHERE employee_id = ?".format(what_to_update), (update, int(employee_id)))


def process_input(c, command):
    if command == "list_employees":
        list_employees(c)

    elif command == "monthly_spending":
        monthly_spending = get_monthly_spending(c)
        print(monthly_spending)

    elif command == "yearly_spending":
        yearly_spending = get_yearly_spending(c)
        print(yearly_spending)

    elif command == "add_employee":
        add_employee(c)

    elif command.startswith("delete_employee"):
        id_of_employee_to_fire = command.split()[1]
        delete_employee(c, id_of_employee_to_fire)

    elif command.startswith("update_employee"):
        employee_id = command.split()[1]
        update_employee(c, employee_id)


def greet_user():
    print("Welcome to CompanyManager(tm).")


def main():
    greet_user()
    connection = sqlite3.connect("company.db")
    c = connection.cursor()
    while True:
        command = input("Enter command> ")
        process_input(c, command)
        connection.commit()

if __name__ == '__main__':
    main()
