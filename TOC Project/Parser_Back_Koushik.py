# Define the grammar as a dictionary of production rules
grammar = {
    'S': ['aAB'],
    'A': ['b'],
    'B': ['c']
}

# Define the input string
#input_string = "abc"  # this will produce "Parsing Successful Result"

input_string = "abbc" # this will produce "Parsing unsuccessful result"



# Create a stack for parsing
stack = ['$', 'S']  # $ is the end-of-input marker

print("Grammar:")
for non_terminal, productions in grammar.items():
    print(f"{non_terminal} -> {' | '.join(productions)}")

print("\nInput String:", input_string)
print("\n")

def parse():
    index = 0  # Current index in the input string

    while stack:
        current_symbol = stack.pop()
        if current_symbol == '$':
            if index == len(input_string):
                print("Parsing successful!")
            else:
                print("Parsing failed! Unprocessed input remains.")
            break
        elif current_symbol.isupper():
            # Non-terminal symbol
            if current_symbol in grammar:
                productions = grammar[current_symbol]
                for production in productions:
                    # Push productions in reverse order onto the stack
                    stack.extend(reversed(list(production)))
        else:
            # Terminal symbol
            if current_symbol == input_string[index]:
                index += 1
            else:
                print("Parsing failed! Mismatched terminal symbol.")
                break

# Start parsing
parse()
