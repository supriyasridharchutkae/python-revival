def palindrome(word):
    
    reverse=word[::-1]
    if(reverse===word):
        return "The word is a palindrome"
    else:
        return "the word is not a palindrome"

word=input("Please enter a word to check if it is a palindrome")
print(palindrome(word))