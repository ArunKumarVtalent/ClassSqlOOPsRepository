# Employee Model class / DB Entity Class

# Here call name is representing Employee Table name in the database
# Each attribute is representing each column of the Employee Table in the database

class Employee:
    def __init__(self, empId, ename, password, gender, dob, phone, email, salary, address, deptNo):
        self.empId = empId
        self.ename = ename
        self.password = password
        self.gender = gender
        self.dob = dob
        self.phone = phone
        self.email = email
        self.salary = salary
        self.address = address
        self.deptNo = deptNo