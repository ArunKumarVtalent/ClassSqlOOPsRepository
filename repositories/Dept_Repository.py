from abc import ABC, abstractmethod

# Abstract Base Class for Department Repository
class DeptRepository(ABC):
    @abstractmethod
    def insert_department(self, department):
        pass

    @abstractmethod
    def update_department(self, department):
        pass

    @abstractmethod
    def delete_department(self, deptNo):
        pass

    @abstractmethod
    def get_all_departments(self):
        pass

    @abstractmethod
    def get_department_by_deptNo(self, deptNo):
        pass

    @abstractmethod
    def get_departments_by_dname(self, dname):
        pass