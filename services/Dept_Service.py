class DeptService:
    def __init__(self, dept_repository):
        self.dept_repository = dept_repository

    def Insert_department(self, department):
        return self.dept_repository.insert_department(department)
    
    def Update_department(self, department):
        return self.dept_repository.update_department(department)
    
    def Delete_department(self, deptNo):
        return self.dept_repository.delete_department(deptNo)
    
    def Get_all_departments(self):
        return self.dept_repository.get_all_departments()
    
    def Get_department_by_deptNo(self, deptNo):
        return self.dept_repository.get_department_by_deptNo(deptNo)
    
    def Get_departments_by_dname(self, dname):
        return self.dept_repository.get_departments_by_dname(dname)