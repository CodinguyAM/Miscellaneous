import palindromeChecker as pc

def longestFrom(text, index):
    pal = None
    startIndex = index
    endIndex = index
    count = 0
    while startIndex >= 0 and endIndex <= len(text):
        if pc.isPalindrome(pc.onlyalphanum(text[startIndex:endIndex])):
            pal = text[startIndex:endIndex]

        if count % 2 == 0:
            endIndex = endIndex + 1
        else:
            startIndex = startIndex - 1
        count = count + 1
    return pal


def longestPalindrome(text):
    pal = ''
    for i in range(len(text)):
        fpal = longestFrom(text, i)
        if len(fpal) > len(pal):
            pal = fpal
    return pal

if __name__ == '__main__':
    while True:
        text = input("Text to find palindrome in?: ")
        print("Longest Palindrome")
        print(longestPalindrome(text))
