s=input("Enter The String\n")
freq={}
for ch in s:
    if ch in freq:
       freq[ch]=freq[ch]+1
    else:
        freq[ch]=1
print(freq)         