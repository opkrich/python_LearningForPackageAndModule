
customer_info = []

class Customer:
    name = ""
    age = ""
    phone = ""

def insert_info(name,age,phone):
    c = Customer()
    c.name = name
    c.age = age
    c.phone = phone
    customer_info.append(c)

def print_info():
    for customer in customer_info:
        print(customer.name + " " + customer.age + " " + customer.phone)