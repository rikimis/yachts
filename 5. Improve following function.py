# 5. Improve following function

def multiply(x,y):
    if(y > 0):
        return 1 + multiply(x, y-1)
    else:
        return 0

print(multiply(2,3)) #3
print(multiply(6,6)) #6
print()

#########################################

def multiply1(x,y):
    result = 0
    while(y > 0):
        result += 1
        y -= 1
    return result


print(multiply1(2,3)) #3
print(multiply1(6,6)) #6
