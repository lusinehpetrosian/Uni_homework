#1
# nums = [1,2,3,4,5,6,7,8]
# k = int(input())%len(nums)
# i = len(nums)
# for r in range(k):
#     digit = nums[i-1]
#     nums.pop(i-1)
#     nums = [digit] + nums
# print(nums)


#2
# nums1 = [1,2,4,5,5,6]
# nums2 = [1,3,5,7,9]
# nums1s = set(nums1)
# nums2s = set(nums2)
# print(nums1s & nums2s)

#3
# nums = [1,2,3,4,5,6,7]
# newlist = []
# s = 0
# for i in range(len(nums)):
#     s+=nums[i]
#     newlist.append(s)
# print (newlist)

# #4?????
# s = input()
# stack = []
# for i in range(len(s)):
#     if (s[i] == '{' or s[i] == '[' or s[i] == '('):
#         stack.append(s[i])
#     elif (s[i] == '}' or s[i] == ']' or s[i] == ')'):
#         if(stack == []):
#             print("They are not equal!")
#             break;
#         elif (stack =! []):
    
    
    
# the right one

# stack = []
# check = '{{][]()][][]}}'
# dct={
#          "{": "}",
#          "(": ")",
#          "[": "]",
#     }

# flag = True

# for c in check:
#     if c in '{[(':
#         stack.append(c)
       
#     else:
#         if len(stack) == 0:
#             flag = False
#             break
#         elif c != dct[stack.pop()]:
#             flag = False   
#             break      
# print(flag) 


