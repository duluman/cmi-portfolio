variable1 = 1000

def isAnagram(s1, s2):
    print(s1, s2)
    if len(s1) != len(s2):
        return False
    
    s1 = sorted(s1)
    s2 = sorted(s2)
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            return False
    
    return True