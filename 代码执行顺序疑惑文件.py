# 2025.02.26

# 声明函数
def index():
    print('视图被执行了')

# 声明函数，并传递形参（形参的作用是占位）
def process_request(view):
    print('执行1')
    view()
    print('执行2')


if __name__ == '__main__':
    process_request(index)

"""
代码执行流程讲解：
    首先要明白几个概念
    1. 函数的声明和调用，形参和实参
        def function_name('形参')： 这是再声明函数，并传递形参
        function_name('实参')   这是在调用函数，并传递实参
    2. 一等公民
        指的是函数数可以像普通数据（如整数、字符串、列表等）一样被使用，函数可以被赋值给变量、作为参数传递给其他函数、作为函数的返回值返回以及存储在数据结构中
    3. 由于存在指代关系 view指代的就是 view(), 但是在代用的时候 实参是index--> 指代的是index()函数，此时index()作为变量 index 赋值给形参 view,
        又因为view指代了 view()函数， 所以   view = view() index = index() view = index  view() = index()

        def process_request(view):
            print('执行1')
            view()
            print('执行2')
            此时形参 view指代的是view()函数
"""