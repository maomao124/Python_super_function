"""
 * Project name(项目名称)：Python_super函数
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/27 
 * Time(创建时间)： 13:22
 * Version(版本): 1.0
 * Description(描述)：
 尽可能避免使用多继承，可以使用一些设计模式来替代它；
super 的使用必须一致，即在类的层次结构中，要么全部使用 super，要么全不用。混用 super 和传统调用是一种混乱的写法；
如果代码需要兼容 Python 2.x，在 Python 3.x 中应该显式地继承自 object。在 Python 2.x 中，没有指定任何祖先地类都被认定为旧式类。
调用父类时应提前查看类的层次结构，也就是使用类的 __mro__ 属性或者 mro() 方法查看有关类的 MRO。
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


class Person(People, Animal):
    # 自定义构造方法
    def __init__(self, name, food):
        # 调用 People 类的构造方法
        super().__init__(name)
        # super(Person,self).__init__(name) #执行效果和上一行相同
        # People.__init__(self,name)#使用未绑定方法调用 People 类构造方法
        # 调用其它父类的构造方法，需手动给 self 传值
        Animal.__init__(self, food)


if __name__ == '__main__':
    per = Person("张三", "熟食")
    per.say()
    per.display()
