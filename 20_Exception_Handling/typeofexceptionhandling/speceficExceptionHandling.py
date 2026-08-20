'''Specific Exception Handling It Is A Type Of Exception Handling Were We 
Alredy Awre Of The Error Which Will Be Occur In Program'''
try:
    a=int(input("Enter The Number"))
    b=int(input("Enter The Nunmber"))
    print(a/b)
except ZeroDivisionError: #Here We Alerdy Kown About Which Type Of Exception Will Be Ocuur So That We Speciflicly Mention The Name of Exception For the Handling that exception
    print("Exception is Handled")