vowel = "aeiouAEIOU"
a = input()
print("".join([x for x in a if x not in vowel]))
