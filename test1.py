"""
 * Project name(项目名称)：Python_super函数
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/27 
 * Time(创建时间)： 13:19
 * Version(版本): 1.0
 * Description(描述)： 
 """


class People:
    def __init__(self, name):
        self.name = name

    def say(self):
        print("我是人，名字为：", self.name)


class Animal:
    def __init__(self, food):
        self.food = food

    def display(self):
        print("我是动物,我吃", self.food)


# People中的 name 属性和 say() 会遮蔽 Animal 类中的
class Person(People, Animal):
    pass


if __name__ == '__main__':
    per = Person("张三")
    per.say()
    # per.display()
