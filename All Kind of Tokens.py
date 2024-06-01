import re

def extract_numbers_from_c_program(c_code):
    number_pattern = r'[-+]?\b\d+\.\d+\b|\b\d+\b|\b\d+\.\d+e[-+]?\d+\b|\b\d+e[-+]?\d+\b'
    numbers = re.findall(number_pattern, c_code)
    return numbers,len(numbers)


def count_keywords(c_code):
    c_keywords = ["auto", "break", "case", "char", "const", "continue",
                    "default", "do", "double", "else", "enum", "extern",
                    "float", "for", "goto", "if", "int", "long", "register",
                    "return", "short", "signed", "sizeof", "static", "struct",
                    "switch", "typedef", "union", "unsigned", "void", "volatile",
                    "while"]
    keyword_pattern = r'\b(?:' + '|'.join(re.escape(keyword) for keyword in c_keywords) + r')\b'
    keyword_matches = re.findall(keyword_pattern, c_code)
    keyword_count = len(keyword_matches)
    return keyword_matches, keyword_count

def extract_special_symbols_from_c_program(c_code):
    special_symbol_pattern = r'[^\w\s]'
    special_symbols = re.findall(special_symbol_pattern, c_code)
    return special_symbols,len(special_symbols)

def extract_operators_from_c_program(c_code):
    operator_pattern = r'[+\-*/%=<>!&|^\?~:]'
    operators = re.findall(operator_pattern, c_code)
    return operators,len(operators)

def extract_user_defined_identifiers_from_c_program(c_code):
    user_iden=[]
    identifier_pattern = r'\b[a-zA-Z_]\w*\b'
    identifiers = re.findall(identifier_pattern, c_code)
    predefined=['include','stdio','h','main','conio',"auto", "break", 
                    "case", "char", "const", "continue","default", 
                    "do", "double", "else", "enum", "extern","float", 
                    "for", "goto", "if", "int", "long", "register",
                    "return", "short", "signed", "sizeof", "static", "struct",
                    "switch", "typedef", "union", "unsigned", "void", "volatile",
                    "while"]
    for identifier in identifiers:
        if identifier not in predefined:
            user_iden.append(identifier)

    return user_iden,len(user_iden)

def count_tokens(c_code):
    token_pattern = r'\b(int|char|float|double|if|else|for|while|do|return|[a-zA-Z_][a-zA-Z0-9_]*|[+\-*/%=><&|!]+|"[^"]*"|\'[^\']\'|0x[0-9a-fA-F]+|-?\d+(\.\d+)?([eE][-+]?\d+)?)\b'
    token_matches = re.findall(token_pattern, c_code)
    token_count = len(token_matches)
    return token_count




c_code = """
#include <stdio.h>
void myFunction() {
    }
int main() {
    int a = 10;
    double b = 3.14;
    float c = 2.718;
    long long d = 1234567890;
    for (int i = 0; i < 10; i++) {
        printf("Hello, World!\n");
    }
    if (a == 10) {
        printf("a is equal to 10\n");
    }
    
    return 0;
}
"""



print("\n__________________________________________________________________________\n")
numbers,num_len = extract_numbers_from_c_program(c_code)
print(f"Total Number of Numbers are: {num_len} \nNumber are:{numbers}")
print("\n__________________________________________________________________________\n")

found_keywords, keyword_count = count_keywords(c_code)
print(f"Total Number of Keywords are: {keyword_count} \nKeyword are:{found_keywords}")
print("\n__________________________________________________________________________\n")

special_symbols,specia_count = extract_special_symbols_from_c_program(c_code)
print(f"Total Number of Special Symbols are: {specia_count} \nSpecial Symbols are:{special_symbols}")
print("\n__________________________________________________________________________\n")

operators,op_count = extract_operators_from_c_program(c_code)
print(f"Total Number of Operators are: {op_count} \nOperators are:{operators}")
print("\n__________________________________________________________________________\n")

user_defined_identifiers,user_defined_count = extract_user_defined_identifiers_from_c_program(c_code)
print(f"Total Number of User Define Identifiers are: {user_defined_count} \nUser Define Identifiers are:{user_defined_identifiers}")
print("\n__________________________________________________________________________\n")


token_count = count_tokens(c_code)
print(f"Total Number of Tokens are: {token_count}")
print("\n__________________________________________________________________________\n")
