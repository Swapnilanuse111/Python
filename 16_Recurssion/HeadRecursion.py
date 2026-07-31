def demo(n):
    if n==0:
        return
    demo(n-1) # in this case the head recurssion call itself agin and again until the basse condtion is true
    print(n) #and then come out of the base condtion and print the valuese
demo(5)