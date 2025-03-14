"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def dfs(emp):
            imp = employee[emp].importance
            for nei in employee[emp].subordinates:
                imp += dfs(nei)
            
            return imp
        
        employee = {emp.id: emp for emp in employees}
        return dfs(id)