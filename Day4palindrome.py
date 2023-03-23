# checking for palindrome
def Palindrome(scan):
    for i in range(0, int(len(scan) / 2)):  # dividing string into 2
        if scan[i] != scan[len(scan) - i - 1]:  # checking 1st and last letter
            return False
    return True
word = "peep"  # Word to check
result = Palindrome(word)
if result:
    print("Yes a Palindrome")
else:
    print("Not a Palindrome")

