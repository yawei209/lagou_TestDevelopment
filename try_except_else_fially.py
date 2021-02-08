
# try:
#     num1 = int(input("清输入第一个数："))
#     num2 = int(input("请输入第二个数："))
#     print(num1/num2)
# except:
#     print("这是一个异常")
# else:
#     print("没有异常。")
# finally:
#     print("程序已停止")

class MyException(Exception):
    def __init__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2

raise MyException("a","b")