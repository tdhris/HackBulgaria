import sqlite3


def create_table(cursor):
    cursor.execute('''create table company
        (employee_id, name, monthly_salary, yearly_bonus, position)''')


def insert(data_item, cursor):
    employee_id = data_item["employee_id"]
    name = data_item["name"]
    monthly_salary = data_item["monthly_salary"]
    yearly_bonus = data_item["yearly_bonus"]
    position = data_item["position"]

    cursor.execute("INSERT INTO company VALUES(?, ?, ?, ?, ?)",
                  (employee_id, name, monthly_salary, yearly_bonus, position))

data = [{
    "employee_id": 1,
    "name": "Ivan Ivanov",
    "monthly_salary": 5000,
    "yearly_bonus": 10000,
    "position": "Software Developer"
}, {
    "employee_id": 2,
    "name": "Rado Rado",
    "monthly_salary": 500,
    "yearly_bonus": 0,
    "position": "Technical Support Intern"
}, {
    "employee_id": 3,
    "name": "Ivo Ivo",
    "monthly_salary": 10000,
    "yearly_bonus": 100000,
    "position": "CEO"
}, {
    "employee_id": 4,
    "name": "Petar Petrov",
    "monthly_salary": 3000,
    "yearly_bonus": 1000,
    "position": "Marketing Manager"
}, {
    "employee_id": 5,
    "name": "Maria Georgieva",
    "monthly_salary": 8000,
    "yearly_bonus": 10000,
    "position": "COO"
}]

connection = sqlite3.connect("company.db")
c = connection.cursor()

create_table(c)

for item in data:
    insert(item, c)

connection.commit()
connection.close()