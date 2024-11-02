# Program to generate Palindrome list

def is_palindrome(num):
    rev = 0
    temp = num
    while num > 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
    return rev == temp


# num = int(input("Enter a number to check Palindrome\n: "))
palindrome_count = int(input("Enter the number of Palindromes you want to print: "))


# if is_palindrome(num):
#     print(f"{num} is a Palindrome.")
# else:
#     print(f"{num} is not a Palindrome.")

print(f"Generating palindromes for list of {palindrome_count} elements.")

palindromes = []
current_num = 1

while len(palindromes) < palindrome_count:
    if is_palindrome(current_num):
        palindromes.append(current_num)
    current_num += 1

print("Generated Palindromes: ", palindromes)


 