def expand_string(input_string):
    result = ""
    i = 0
    while i < len(input_string):
        # Check if the current character is a letter
        if input_string[i].isalpha():
            char = input_string[i]
            i += 1
            num = ""
            # Collect all digits following the letter
            while i < len(input_string) and input_string[i].isdigit():
                num += input_string[i]
                i += 1
            # Repeat the character according to the number
            result += char * int(num)
    return result

# Example usage:
input1 = "a1b10"
input2 = "a2b4c6"

print(expand_string(input1))  # Output: abbbbbbbbbb
print(expand_string(input2))  # Output: aabbbbcccccc
