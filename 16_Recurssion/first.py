#recursion it is a process of function calling itself again and again until the base condition or termiantion conditioin becomes true
def add(n):
    if n==0:
        return 
    add(n-1) 
print(add(5))