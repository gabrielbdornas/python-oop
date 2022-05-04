from employee import Employee

class Developer(Employee):
  def __init__(self, first_name, last_name, pay, language):
    super().__init__(first_name, last_name, pay)
    self.language = language

empl_1 = Developer('Maria', 'José', 50000, 'Python')
print(empl_1)
