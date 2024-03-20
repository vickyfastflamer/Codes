class person:
    name=""
    age=0
    def introduce(self):
        print("personal information")
        print("My name is:",self.name,"My age:",self.age)

person2=person()
person2.name="Panda"
person2.age=20
person2.introduce()

class book:
    title=""
    author=""
    year=0
    def display(sel):
        print("book information")
        print("title:",sel.title,"\n author:",sel.author,"\n year of publishing:",sel.year)

book1=book()
book1.title="Atomic habits"
book1.author="James clear"
book1.year=2018
book1.display()
