#Multiple Inheritance
# Father class created
class Father:
    fathername = ""
 
    def show_father(self):
        print(self.fathername)
 
 
# Mother class created
class Mother:
    mothername = ""
 
    def show_mother(self):
        print(self.mothername)
 
 
# Son class inherits Father and Mother classes
class Son(Father, Mother):
    def show_parent(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
 
 
s1 = Son()  # Object of Son class
s1.fathername = "Sorab"
s1.mothername = "Sonia"
s1.show_parent()