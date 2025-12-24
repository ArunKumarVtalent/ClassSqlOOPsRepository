# Department Model class / DB Entity Class

# Here call name is representing Department Table name in the database
# Each attribute is representing each column of the Department Table in the database

class Department:
    def __init__(self, deptNo, dname, location):
        self.deptNo = deptNo
        self.dname = dname
        self.location = location
