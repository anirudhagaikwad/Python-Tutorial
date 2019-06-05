#hierarchical Inheritance
# Parent class created
class Parent:
    parentname = ""
    childname = ""
 
    def show_parent(self):
        print(self.parentname)
 
 
# Son class inherits Parent class
class Son(Parent):
    def show_child(self):
        print(self.childname)
 
 
# Daughter class inherits Parent class
class Daughter(Parent):
    def show_child(self):
        print(self.childname)
 
 
s1 = Son()  # Object of Son class
s1.parentname = "Vasudev"
s1.childname = "Krishna"
s1.show_parent()
s1.show_child()
 
d1 = Son()  # Object of Daughter class
d1.childname = "Riya"
d1.parentname = "Vasudev"
d1.show_parent()
d1.show_child()