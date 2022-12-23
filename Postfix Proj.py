# converting postfix to infix By amirabbas gashtil and saba sarmadi 

stack = []
ops = ['*', '/', '+', '-']
parenthesis = ['(', ')']
counter = 0
str = input()
tmp_str = ''

strList = []

# converting string to list
for char in str:
    strList.append(char)

# replace an item in ops with previous item in stack
for i in range(len(str)):

    if strList[i] in ops:

        tmp_str = strList[i - 1]
        strList[i - 1] = strList[i]
        strList[i] = tmp_str
        stack.pop()
        stack.append(strList[i - 1])
        stack.append(strList[i])

    elif strList[i] in parenthesis:
        stack.append(str[i])

    else:
        stack.append(str[i])

finalstring = ''

for item in stack:

    finalstring += item

print(finalstring)
