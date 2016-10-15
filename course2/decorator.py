def multiply(times):
    def repeat(func):
        def new_func(*args, **kwds):
            for _ in range(times):
                func(*args, **kwds)

        return new_func

    return repeat


@multiply(10)
def log():
    print 'hi'


log()
