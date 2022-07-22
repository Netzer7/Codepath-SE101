def reverse_vowels(string):
    # Write your code here
    vowels = ['a', 'e', 'i', 'o', 'u']
    s = list(string)
    ptr1 = 0
    ptr2 = len(s) - 1

    while ptr1 <= ptr2:
        frstVowel = -1
        scndVowel = -1
        if s[ptr1] in vowels:
            frstVowel = ptr1
            ptr1 -= 1
        if s[ptr2] in vowels:
            scndVowel = ptr2
            ptr2 += 1
        if (frstVowel != -1 and scndVowel != -1):
            temp = s[frstVowel]
            s[frstVowel] = s[scndVowel]
            s[scndVowel] = temp
            ptr1 += 1
            ptr2 -= 1
        ptr1 += 1
        ptr2 -= 1
    return "".join(s)

print(reverse_vowels("hello"))
print(reverse_vowels("leetcode"))
