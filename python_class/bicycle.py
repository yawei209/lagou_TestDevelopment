# -*- coding: utf-8 -*-
# @Time : 2021/2/11 21:24
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : bicycle.py
# @Software: PyCharm


#自行车类
class Bicycle:
    def run(self, km):
        print(f"用脚蹬了{km}公里，好累呀！")

#电动自行车类
class Ebicycle(Bicycle):
    #构造函数，定义电动自行车的点量
    def __init__(self, valume):
        self.valume = valume


    #充电方法
    def fill_charge(self, vol):
        self.valume = self.valume + vol
        print(f"充了{vol}度点，现在的电量为{self.valume}度.")
    '''
    
    '''
    def run(self, km):
        #power_km 电车用电的历程
        power_km = self.valume*10

        if power_km >= km:
            print(f"我用电动车骑行了{km}公里")

        else:
            print(f"我电动车骑了{power_km}公里之后没电了，")
            #super()函数的作用是能够调用父类的方法
            super().run(km - power_km)

# bike = Bicycle()
# bike.run(10)

ebike = Ebicycle(2)
# ebike.fill_charge(5)
ebike.run(40)