
import os

# abs_path = os.path.abspath(".")
# print(abs_path)
#
# file = os.path.join(abs_path, "file")
# print(os.path.join(abs_path, "file"))
#
# print(os.path.split(file))

# print(os.listdir())

# try:
#     os.mkdir("file")  #创建文件夹
# except:
#     print("文件已存在")
#
# print(os.listdir())

# os.rmdir("file")    #删除文件夹


# print(os.listdir())

# print(os.path.isfile(file))
# print(os.path.isdir(file))
# print(os.path.splitext(file)[1])


# try:
#     os.mkdir("file")  #创建文件夹
# except:
#     print("文件已存在")
#
# print(os.listdir())
#
# list_dir = [x for x in os.listdir('.') if os.path.isdir(x)]
# print(list_dir)
#
# list_py = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)]
# print(list_py)

# if not os.path.exists("file"):
#     os.mkdir("file")
#
# if not os.path.exists("file/test.txt"):
#     f = open("file/test.txt", 'w')
#     f.write("OS useing!")
#     f.close()

path_cwd = os.getcwd()
os.remove("file/test.txt")
os.removedirs("file")