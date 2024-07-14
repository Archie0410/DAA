class Solution(object):
    def average(self, salary):
        min_salary = min(salary)
        max_salary = max(salary)
        total_salary = sum(salary) - min_salary - max_salary
        n = len(salary) - 2
        return total_salary / n