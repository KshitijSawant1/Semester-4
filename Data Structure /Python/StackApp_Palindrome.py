input_string = input("Enter input to check if Palindrome : ")
n = len(input_string)
stack1 = []
stack2 = []

for char in input_string:
    stack1.append(char)

print("Stack 1 after pushing elements:", stack1)

for i in range(len(stack1)-1, -1, -1):
    item = stack1[i]
    stack2.append(item)
    
print("Stack 2 after pushing elements:", stack2)

flag = True  # Assume it's a palindrome initially
for i in range(n):
    # Pop elements from both stacks for comparison
    if stack1[i] == stack2[i]:
        flag = True
    else : 
        flag = False
        break

    
# Result based on the flag
if flag:
    print("The input is a palindrome.")
else:
    print("The input is not a palindrome.")