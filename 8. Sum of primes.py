# 8. Sum of primes

result = []

def isPrime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return False
        else:
            return True
    return False

def isPrimeList(lis):
    for item in lis:
        if(isPrime(item) == False):
            return False
    return True

def findCombinationsUtil(lis, index, num, reduced):
 
    if (reduced < 0):
        return
 
    if (reduced == 0):
        helper = []
        for i in range(index):
            helper.append(lis[i])
        if(len(helper) > 1):
            result.append(helper)
        return
 
    prev = 1 if(index == 0) else lis[index - 1]

    for k in range(prev, num + 1):
        lis[index] = k
        findCombinationsUtil(lis, index + 1, num, reduced - k)
 
def findCombinations(n):
    result.clear()
    result2 = []
    lis = [0] * n
    findCombinationsUtil(lis, 0, n, n)
    for item in result:
        if(isPrimeList(item)):
            result2.append(item)
    #print(result2) #<-- all combinations
    return len(result2)
 

print(findCombinations(4)) # = 1
print(findCombinations(5)) # = 1
print(findCombinations(6)) # = 2
print(findCombinations(7)) # = 2
print(findCombinations(8)) # = 3
print(findCombinations(9)) # = 4


