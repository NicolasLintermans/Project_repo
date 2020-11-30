employee_id_dict = {
    'employee1_ID': -1,
    'employee2_ID': 0,
    'employee3_ID': 1
}


def update_employee_id(value):      # we want the ID's to start from 1, instead of -1
    return value + 2


updated_employee_id = list(map(update_employee_id, employee_id_dict.values()))      # correct version
updated_employee_dict = dict(zip(employee_id_dict.keys(), updated_employee_id))     # zip keys with correct version
print(updated_employee_dict)

employee_authentication_dict = {        # employee 1 and 2 have access to the databases, employee 3 not
    'employee1_ID': True,
    'employee2_ID': True,
    'employee3_ID': False
}


def authenticator(function):            # authenticator (for database) decorator
    def wrap(*args, **kwargs):          # wrap function iterates through the dictionary and checks whether user has access
        for keys, values in employee_authentication_dict.items():
            if values:
                print(f'{keys}: {function(*args, **kwargs)}')   # if access: do what 'function' tells you to do
            else:
                print(f'{keys}: You have no access.')           # if no access: print 'no access'
    return wrap


@authenticator                         # 'call' decorator
def access_database(user):
    return 'Access granted'


access_database(employee_authentication_dict.values())


class Employee:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def greeting_employee(self):
        print(f'Hello {self.name}!')


class Customer:
    def __init__(self, id, name, email, balance):
        self.id = id
        self.name = name
        self.email = email
        self.balance = balance

    def customer_purchase(self, cost):
        if cost > self.balance:
            print("Your balance does not allow this.")
        else:
            print(f"Thank you for your purchase! You still have {self.balance-cost} on your account")


class Hybrid(Employee, Customer):
    def __init__(self, id, name, email, balance):
        Employee.__init__(self, id, name, email)
        Customer.__init__(self, id, name, email, balance)

    def employee_purchase(self, cost):
        employee_discount = 0.05
        employee_cost = cost * (1 - employee_discount)
        if employee_cost > self.balance:
            print("Your balance does not allow this.")
        else:
            print(f"Thank you for your purchase! You still have {self.balance-employee_cost} on your account")


employee1 = Employee(1, 'Nicolas Lintermans', 'nl@gmail.com')
employee1.greeting_employee()

customer1 = Customer(1, 'Lintermans Nicolas', 'ln@gmail.com', 500)
customer1.customer_purchase(200)

hybrid1 = Hybrid(1, 'NL', 'NL@gmail.com', 500)
hybrid1.employee_purchase(200)


# example of output:
# {'employee1_ID': 1, 'employee2_ID': 2, 'employee3_ID': 3}

# employee1_ID: Access granted
# employee2_ID: Access granted
# employee3_ID: You have no access.

# Hello Nicolas Lintermans!
# Thank you for your purchase! You still have 300 on your account
# Thank you for your purchase! You still have 310.0 on your account
#
# Process finished with exit code 0
