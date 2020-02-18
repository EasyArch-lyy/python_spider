# 定义函数,有多个返回值(返回元组)
def measure():
    """测量温度和湿度"""

    print("测量开始...")
    temp = 39
    wetness = 50
    print("测量结束...")

    # 元组-可以包含多个数据，因此可以使用元组让函数一次返回多个值
    # 如果函数返回的类型是元组，小括号可以省略
    # return (temp, wetness)
    return temp, wetness  # 小括号可以省略


# 元组
result = measure()
print(result)  # (39, 50)

# 需要单独的处理温度或者湿度 - 不方便
print(result[0])  # 39
print(result[1])  # 50

# 如果函数返回的类型是元组，同时希望单独的处理元组中的元素
# 可以使用多个变量，一次接收函数的返回结果
# 注意：使用多个变量接收结果时，变量的个数应该和元组中元素的个数保持一致
gl_temp, gl_wetness = measure()  # 接受函数多个返回值

print(gl_temp)  # 39
print(gl_wetness)  # 50
