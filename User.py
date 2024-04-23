from abc import ABC

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = []

    def view_menu(self, restaurent):
        restaurent.menu.view_menu()

    def add_to_cart(self, restaurent, item_name):
        item = restaurent.menu.find_item(item_name)
        if item:
            pass
        else:
            print('Item not found')

class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        
    def add_employee(self, employee):
        Restaurent.add_employee(employee)

    def view_employee(self, restaurant):
        restaurant.view_employee()

    def add_new_item(self, restaurent, item):
        restaurent.menu.add_menu_item(item)

    def remove_item(self, restaurent, item):
        restaurent.menu.remove_item(item)

class Restaurent:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = FoodItem()

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f'{employee.name} is added !!')

    def view_employee(self):
        print('Employee list: ')
        for emp in self.employees:
            print(emp.name, emp.phone, emp.email, emp.address)

class Menu:
    def __init__(self):
        self.items = []

    def add_menu_item(self, item):
        self.items.append(item)

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None
    
    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print('Item deleted')
        else:
            print('Item not found !')

    def show_items(self):
        print('*****MENU*****')
        print('NAME\tPRICE\tQUANTITY')
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quatity}")

class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    
        