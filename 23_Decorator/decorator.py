def dec_fun(func):
    def wrapper():
        print("This Is Main Task")
        func()
    return wrapper
@dec_fun
def Hello():
    print("This Is Main Block")
print(Hello)