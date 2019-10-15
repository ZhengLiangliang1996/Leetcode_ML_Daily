"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        hashmap = dict()
        res = 0
        
        for employee in employees:
            hashmap[employee.id] = [employee.importance, employee.subordinates]
      
        q = []
        q.append(id)
        while q:   
            next_queue = []
            for item in q:
                res += hashmap[item][0]
                next_queue += hashmap[item][1]
            q = next_queue[:]
            
        return res