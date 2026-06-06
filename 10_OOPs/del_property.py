class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print(f"Object of {self.name} is being deleted")
s1 = student("shivam", 20)
print (s1.name)
del s1
