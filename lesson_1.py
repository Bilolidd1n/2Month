# ''' Абстракция '''
# class Vehicle:
#     def start_engine(self):
#         pass

#     def stop_engine(self):
#         pass

#     def drive(self):
#         pass

# class Car(Vehicle):
#     def start_engine(self):
#         return 'Двигатель автомобиля заведен'
    
#     def stop_engine(slef):
#         return 'Двигатель автомобиля заведен'
    
#     def drive(self):
#         return 'Avto Едет'
    
# class Bycycle(Vehicle):
#     def start_engine(self):
#         return 'У велосипеда нет двигателья'
    
#     def stop_engine(self):
#         return 'У велосипеда нет двигателья'
    
#     def drive(self):
#         return 'Велик Едет'


class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return 0

    def display_info(self):
        print(f"Employee: {self.name},  Базовая ставка {self.base_salary}")

class FullTimeEmployee(Employee):
    def __init__(self, name, base_salary):
        super().__init__(name, base_salary)

    def calculate_salary(self):

        return self.base_salary * 1.2

class PartTimeEmployee(Employee):
    def __init__(self, name, base_salary, hours_worked):
        super().__init__(name, base_salary)
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.base_salary * 0.5 * self.hours_worked

def process_salary(employee):
    employee.display_info()
    salary = employee.calculate_salary()
    print(f"Калкулятор: {salary}\n")

if __name__ == "__main__":
    full_time_emp = FullTimeEmployee("Sodiq Sriq", 500000)
    part_time_emp = PartTimeEmployee("Biloliddin ", 100000, 20)

    process_salary(full_time_emp)
    process_salary(part_time_emp) 

# Описание:
# Ваша задача — создать систему для расчета зарплаты сотрудников, которая демонстрирует абстракцию, наследование и полиморфизм. Не используйте модуль abc, используйте только базовые механизмы Python.

# Требования:  
# Базовый класс Employee:

# Создайте класс Employee с методом calculate_salary(), который возвращает нулевую зарплату по умолчанию. Также добавьте метод display_info(), который выводит информацию о сотруднике.
# Конструктор класса должен принимать имя сотрудника и его базовую ставку.
# Классы-наследники для разных типов сотрудников:

# Создайте классы FullTimeEmployee и PartTimeEmployee, которые наследуются от класса Employee.
# Для класса FullTimeEmployee метод calculate_salary должен возвращать зарплату как базовую ставку умноженную на фиксированный коэффициент (например, 1.2).
# Для класса PartTimeEmployee метод calculate_salary должен возвращать зарплату как базовую ставку умноженную на коэффициент, зависящий от количества отработанных часов (например, базовая ставка умноженная на 0.5 за каждый час).
# Использование полиморфизма:

# Создайте функцию process_salary(employee), которая принимает объект типа Employee и вызывает его методы calculate_salary и display_info.
# Функция должна корректно работать для всех производных классов, демонстрируя полиморфизм.'''