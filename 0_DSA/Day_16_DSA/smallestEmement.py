# arr=[20,30,7,9,3]
# # min=arr[0]
# # index=0
# # for i in range(len(arr)):
# #     for i in arr:
# #         if i<min:
# #             min=i            
# # print(min)

arr=[20,30,7,9,3]
# min=arr[0]
# for i in range(len(arr)):
#     if i<min:
#         min=i
# print(min)



min=arr[0]
for i in range(len(arr)):
    if min>i:
        min=i
print(min)
