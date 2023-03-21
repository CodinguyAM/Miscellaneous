def onlyalphanum(text):
    text = text.lower()
    r = ''
    for letter in text:
        if letter in 'qwertyuiopasdfghjklzxcvbnm1234567890':
            r = r + letter
    return r

def isPalindrome(text):
    #single or no letters
    if len(text) < 2:
        return True
    firstLetter = text[0]
    lastLetter = text[-1]
    midLetters = text[1:-1]

    #cases like 'motor'
    if firstLetter != lastLetter:
        return False
    else:
        return isPalindrome(midLetters)

def testCases():
    
    assert isPalindrome('catty') == False
    assert isPalindrome('motor') == False
    assert isPalindrome('rotor') == True

if __name__ == "__main__":
    testCases()
    while True:
        text = input("What text would you like to check?: ")
        if isPalindrome(onlyalphanum(text)):
            print("That's a palindrome!")
        else:
            print("Sorry, that's not a palindrome.")
        print()
