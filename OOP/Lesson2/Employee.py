from datetime import datetime, timedelta


class Employee:
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

    def work(self):
        return "I come to the office."

    def check_salary(self, days):
        return f"Salary for {days} days - {days*self.salary}"

    def check_salary_now(self):
        start = datetime(datetime.now().year, datetime.now().month, 1)
        # end = datetime.today()
        end = datetime(2022, 9, 16)
        # delta = []
        # for i in range((end - start).days + 1):
        #     delta.append(start + timedelta(i))
        delta = [start + timedelta(i) for i in range((end - start).days + 1)]
        # amount = 0
        # for j in delta:
        #     if j.weekday() < 5:
        #         amount += 1
        amount = sum(1 for j in delta if j.weekday() < 5)
        return f"Salary for today({amount} days) - {amount*self.salary}"

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __ne__(self, other):
        return self.salary != other.salary


class Recruiter(Employee):
    def __init__(self, name: str, salary: int):
        super().__init__(name, salary)

    def work(self):
        return "I come to the office and start to hiring."

    def __str__(self):
        return f"{__class__.__name__}: {self.name}"


class Developer(Employee):
    def __init__(self, name: str, salary: int, tech_stack: list):
        self.tech_stack = tech_stack
        super().__init__(name, salary)

    def work(self):
        return "I come to the office and start to coding."

    def __str__(self):
        return f"{__class__.__name__}: {self.name}"

    def __lt__(self, other):
        return len(self.tech_stack) < len(other.tech_stack)

    def __le__(self, other):
        return len(self.tech_stack) <= len(other.tech_stack)

    def __gt__(self, other):
        return len(self.tech_stack) > len(other.tech_stack)

    def __ge__(self, other):
        return len(self.tech_stack) >= len(other.tech_stack)

    def __eq__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)

    def __ne__(self, other):
        return len(self.tech_stack) != len(other.tech_stack)


if __name__ == '__main__':
    dev = Developer("Liam", 80, ["python", "php", "js", "C#", "Go"])
    dev2 = Developer("Aren", 100, ["python", "java", "js", "ruby", "C"])
    print(dev.__str__())
    print(dev.check_salary(16))
    print(dev2.check_salary_now())
    dev3 = Developer(dev.name + " " + dev2.name, max(dev.salary, dev2.salary),
                     list(set(dev.tech_stack + dev2.tech_stack)))
