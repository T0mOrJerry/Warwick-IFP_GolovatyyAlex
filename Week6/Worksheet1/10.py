def check_palindrome(a: str):
    if a == a[::-1]:
        return True
    return False


str_to_check = input()
print(check_palindrome(str_to_check))