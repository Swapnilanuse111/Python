#it is a type of recursion which call where the recursive call is made as the last statment of the function
def fun(n):
    if n==0: 
    #1st check 5==0 is false then gose to the print statment and print 5    #base Condition
    #2nd check 4==0 is false then it will gose out of the base condtion and print the 4
        
        return
    print(n) #here 1 print the 5 then teail recurssion is call
    fun(n-1)  #here fun(5-1)=(4) it will gose to the function agin and check the base condition is true or false
fun(5) 
