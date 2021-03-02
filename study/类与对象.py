#coding = utf-8

class Person:
    def __init__(self,age,height):
        # self.age = age
        # self.height = height

        # self.hidden_age = age
        # self.hidden_height = height
        self.age = age
        self.height = height

    def get_age(self):
        return self.age

    # def set_age(self,age):
        self.age = age

    def speak_language(self):
        print('speak in english')

#可以改变属性值
# p = Person(20,180)
# p.age = 40
# print(p.height)
# print(p.age)
# p.speak_language()

#通过改变属性名隐藏
# p = Person(20,180)
# # print(p.height)
# # print(p.age)
# print(p.hidden_age)
# p.speak_language()

#get与set

p = Person(20,180)
print(p.get_age())
# p.set_age(30) #AttributeError: 'Person' object has no attribute 'set_age'
p.age = 50
print(p.get_age())



