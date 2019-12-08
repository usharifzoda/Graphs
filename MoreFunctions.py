# Reverse String

name = 'HelloWorld'
print(name)
print(name[::-1])

vals = [15, 2, 5, 6, 13, 3]
max = 0
i = 0
for x in vals:
    if vals[i] > max:
        max = vals[i]
        i += 1


print(max)

#Find Palindrome

word = 'racecar'

def isPalindrome(w):
    print(w)
    start = 0
    end = len(w)-1
    #print(w[end])

    if(w[start] != w[end]):
        return False
    start +=1
    end +=1

    return True

print(isPalindrome(word))