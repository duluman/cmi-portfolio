x = input()

def palindrom(p):
    y = ""
    for i in range(0, len(p)):
        y += p[len(p)-i-1]

    if y == p:
        return True
    else:
        return False

print(palindrom(x))

def palindrome3(x):
    b = x[::-1]
    if x == b:
        print(f' {x} is a palindrome.')
        return True
    else:
        print(f' {x} is not a palindrome.')
        return False


mesaj2 = 'radar'
c = palindrome3(mesaj2)

mesaj3 = 'castane'
d = palindrome3(mesaj3)

is_p = lambda x: x == x[::-1]
print(is_p('ana'))

def is_palindrom(s):
    s2 = ""
    n = len(s)
    while n >= 1:
        s2 += s[n-1]
        n -= 1
    return s == s2

print(is_palindrom('ana'))