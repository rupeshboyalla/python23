"""

Decode string
"3[a2[c]]" i



"""





def decode_string(s):
    stack = []
    current_num = 0
    current_str = ''

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_str, current_num))
            current_str = ''
            current_num = 0
        elif char == ']':
            prev_str, num = stack.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += char

    return current_str

# Example usage:
input_str = "3[a2[c]]"
decoded_str = decode_string(input_str)
print(decoded_str)  # Output: "accaccacc"
