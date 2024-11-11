class Person:
  def __init__(self, fname, lname,address,age):
    self.firstname = fname #public
    self.lastname = lname #public
    self._address = address #protected
    self.__age = age #private

  def printname(self):
    print(self.firstname, self.lastname, self._address, self.__age)

  def show_age(self):
    print(self.__age)
