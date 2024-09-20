import re

equation = input("Input equation to be evaluated in y = form:\ny = ")
# generate a 10x10 array for displaying the graph of equation



def insert_multiplication(equation):
    # Regex pattern to find numbers followed by 'x'
    pattern = r'(\d+(\.\d+)?)(x)'
    # Replace the pattern with 'number * x'
    modified_equation = re.sub(pattern, r'(\1 * \2)', equation)
    # Regex pattern to find numbers followed by '(expression)'
    return modified_equation
def evaluate(equation, x):
    equation.replace("x", str(x))
    return eval(equation)

# fix implicit multiplications
equation = insert_multiplication(equation)

print(equation)
print('for x = 1, y = ', evaluate(equation, 1))
array_10x10 = [[" " for _ in range(10)] for _ in range(10)]

#for row in array_10x10:
#    print(row)