import re


def generate_temp():
    global temp_count
    temp_count=0
    temp_count += 1
    return f't{temp_count}'

def generate_three_address_code(expression):
    operators = "+-*/"
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
    stack = []
    output = []
    tokens = re.findall(r'\d+|[-+*/()]|\w+', expression)

    for token in tokens:
        if token.isdigit() or token.isalpha():
            output.append(token)
        elif token in operators:
            while (stack and stack[-1] in operators and precedence[stack[-1]] >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()

    while stack:
        output.append(stack.pop())

    three_address_code = []
    temp_count = 0

    for token in output:
        if token.isdigit() or token.isalpha():
            stack.append(token)
        elif token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            temp = generate_temp()
            three_address_code.append(f"{temp} = {operand1} {token} {operand2}")
            stack.append(temp)

    return three_address_code

if __name__ == "__main__":
    # expression = "a + b * (c - d)"
    expression = input("Enter The Expression:")
    code = generate_three_address_code(expression)

    for line in code:
        print(line)
