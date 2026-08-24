'''Assert Keywrod Can Be Used In order to raise exception based on there condition
    By Using The Assert Keywod We Can Give The Condition Is The Condition Is  
    False In That Time It Will give the Assertion Error


    in the time of giving the condtion We are aslo providing The Error Values Which 
    Time Of Error or Massage will be show to the user after the condtion is false and in the
    time getting the assertion error
'''

# age=int(input("Enter the age"))
# assert age>21
# print("You Are Eligible For Voting Getting Guys")

age=int(input("Enter Youre age "))
assert age>18,"Youre Are Not Eligible For Voting"
print("You Are eligible For voting")