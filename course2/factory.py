def fac(string):
    def my_print():
        print(string)
    return my_print

greeter = fac('Hello')
greeter()