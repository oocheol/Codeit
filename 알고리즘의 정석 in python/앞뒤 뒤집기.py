def is_palindrome(word):
    check = list(word)
    word = list(word)
    
    for left in range(len(word) // 2):
        right = (len(word)-1) - left
        word[left], word[right] = word[right], word[left]
    
    if check == word :
        return True
    
    else :
        return False

# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))