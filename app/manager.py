from employee import Employee

class Manager(Employee):
  def __init__(self, first_name, last_name, pay, employees=[]):
    super().__init__(first_name, last_name, pay)
    self.employees = employees

  def add_dev(self, dev):
    if dev not in self.employees:
      self.employees.append(dev)

  def remove_dev(self, dev):
    if dev in self.employees:
      self.employees.remove(dev)

empl_4 = Manager('João', 'Santos', 70000)
print(empl_4)
