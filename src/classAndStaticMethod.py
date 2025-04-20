class Developer:
    company = "GoCoolTech"  # class-level

    def __init__(self, name):
        self.name = name  # instance-level
        self.skills = []

    def add_skill(self, skill):  # instance method
        self.skills.append(skill)

    def show_profile(self):  # instance method
        print(f"{self.name} ({self.company}) - Skills: {self.skills}")

    @classmethod
    def change_company(cls, new_name):  # class method
        cls.company = new_name

    @staticmethod
    def check():
        print(f"Company Stored")



d1 = Developer("Arjun")
d1.add_skill("Python")
d2 = Developer("Rahul")
d2.add_skill("Java")
d1.show_profile()  
d2.show_profile()  

print('----------Before')
Developer.change_company("GoCoolX")
Developer.check()
d1.show_profile()  
d2.show_profile()                   # reflects updated company
