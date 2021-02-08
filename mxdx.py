
#面向对象编程

#创建一个人类

class Person:
    name = "default_name"
    age = "default_age"
    gender = "default_gender"
    weight = "default_weight"

    def __init__(self,name, age, gender, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    def eat(self):
        print(f"{self.name} is eating")

    def play(self):
        print(f"{self.name} is playing")
        return "playing"

    def jump(self):
        print(f"{self.name} is jump")

zhangyawei = Person("zhangyawei",30, "男", '80kg')

print(f"zhangyawei 的名字是 {zhangyawei.name}")
print(f"zhangyawei can {zhangyawei.play()}")
zhangyawei.eat()