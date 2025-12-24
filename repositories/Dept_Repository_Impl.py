from repositories.Dept_Repository import DeptRepository 

class DeptRepositoryImpl(DeptRepository):   
    def __init__(self, connection):
        self.connection = connection
        
    def insert_department(self, department):
        cursor = self.connection.cursor()
        insert_query = "INSERT INTO Department (DeptNo, Dname, Location) VALUES (%s, %s, %s)"
        try:
            cursor.execute(insert_query, (department.deptNo, department.dname, department.location))
            self.connection.commit() # Commit the transaction to save changes        
            print("Department record inserted successfully.")
        except Exception as e:
            print(f"Error inserting record: {e}")
        finally:
            cursor.close()

    def update_department(self, department):        
        cursor = self.connection.cursor()
        update_fields = []
        params = []
        if department.dname:
            update_fields.append("Dname = %s")
            params.append(department.dname)
        if department.location:
            update_fields.append("Location = %s")
            params.append(department.location)
        params.append(department.deptNo)  # For the WHERE clause    
        update_query = f"UPDATE Department SET {', '.join(update_fields)} WHERE DeptNo = %s"
        try:
            cursor.execute(update_query, tuple(params))
            self.connection.commit() # Commit the transaction to save changes        
            print("Department record updated successfully.")
        except Exception as e:
            print(f"Error updating record: {e}")
        finally:
            cursor.close()

    def delete_department(self, deptNo):
        cursor = self.connection.cursor()
        delete_query = "DELETE FROM Department WHERE DeptNo = %s"
        try:
            cursor.execute(delete_query, (deptNo,))
            self.connection.commit() # Commit the transaction to save changes        
            print("Department record deleted successfully.")
        except Exception as e:
            print(f"Error deleting record: {e}")
        finally:
            cursor.close()

    def get_all_departments(self):
        cursor = self.connection.cursor()
        select_query = "SELECT * FROM Department"
        try:
            cursor.execute(select_query)
            deptList = cursor.fetchall()
            return deptList
        except Exception as e:
            print(f"Error fetching records: {e}")
            return []
        finally:
            cursor.close()

    def get_department_by_deptNo(self, deptNo):
        cursor = self.connection.cursor()
        select_query = "SELECT * FROM Department WHERE DeptNo = %s"
        try:
            cursor.execute(select_query, (deptNo,))
            dept = cursor.fetchone()
            return dept
        except Exception as e:
            print(f"Error fetching record: {e}")
            return None
        finally:
            cursor.close()

    def get_departments_by_dname(self, dname):
        cursor = self.connection.cursor()
        select_query = "SELECT * FROM Department WHERE Dname = %s"
        try:
            cursor.execute(select_query, (dname,))
            deptList = cursor.fetchall()
            return deptList
        except Exception as e:
            print(f"Error fetching records: {e}")
            return []
        finally:
            cursor.close()