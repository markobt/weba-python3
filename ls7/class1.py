# class First:
#     color = "red"
#     def out(self):
#         print(self.color + "!")
#
# obj1 = First()
# obj2 = First()
#
#
# print(obj1.color)
# print(obj2.color)
# obj1.out()
# obj2.out()

class Second:
    color = "red"
    form = "circle"
    cost = 20
    def changecolor(self,newcolor):
        self.color = newcolor
    def changeform(self,newform):
        self.form = newform
    def changecost(self,newcost):
        self.cost = newcost


obj1 = Second()
obj2 = Second()
obj3 = Second()

print(obj1.color, obj1.form, obj3.cost)
print(obj2.color, obj2.form, obj3.cost)


obj1.changecolor("green")
obj1.changecost(50)
obj2.changecolor("blue")
obj2.changeform("oval")
obj3.changecost(100)

print(obj1.color, obj1.form, obj1.cost)
print(obj2.color, obj2.form, obj2.cost)
print(obj3.color, obj3.form, obj3.cost)
