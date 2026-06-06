class student:
    def __init__(self, name, Marks1, Marks2, Marks3):
        self.name = name
        self.Marks1 = Marks1
        self.Marks2 = Marks2
        self.Marks3 = Marks3
    def avg(self):
        return (self.Marks1 + self.Marks2 + self.Marks3) / 3

s1 = student("shivam", 85, 90, 78)
print(s1.avg())