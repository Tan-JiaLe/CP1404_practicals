import datetime


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage =completion_percentage

    def __str__(self):
        start_date = self.start_date.strftime("%d/%m/%Y")
        return f"{self.name}, start: {start_date}, priority {self.priority}, estimate: ${self.cost}, completion: {self.completion_percentage}%"

    def __repr__(self):
        start_date = self.start_date.strftime("%d/%m/%Y")
        return f"{self.name}, start: {start_date}, priority {self.priority}, estimate: ${self.cost}, completion: {self.completion_percentage}%"

    def __lt__(self):
        return self.priority < other.priority

    def is_after_certain_time(self, date):
        return self.start_date >= date