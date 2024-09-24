import re

equation = input("Input equation to be evaluated in y = form:\ny = ")
# generate a 10x10 array for displaying the graph of equation



def insert_multiplication(equation):
    # Regex pattern to find numbers followed by 'x'
    pattern = r'(\d+(\.\d+)?)(x)'
    # Replace the pattern with 'number * x'
    modified_equation = re.sub(pattern, r'(\1 * \3)', equation)
    # Regex pattern to find numbers followed by '(expression)'
    # TODO: Implement this pattern
    return modified_equation
def evaluate(equation, x):
    equation.replace("x", str(x))
    return eval(equation)

# fix implicit multiplications
equation = insert_multiplication(equation)



array_10x10 = [[" " for _ in range(10)] for _ in range(10)]
for i in range(10):
    #print('for x = ', i, ', y = ', evaluate(equation, i))
    solution = int(evaluate(equation, i))
    solution_last_y = int(evaluate(equation, i-1))
    if (solution < 10 and solution >= 0):
        array_10x10[solution][i] = "*"
        
        


# code to nicely display the graph
print("     ", end="")
for _ in range(23):
    print("-", end="")
print()
for i in range(9, -1, -1):
    if i + 1 < 10:
        print(f"{i+1}  - |", end=" ")
    else:
        print(f"{i+1} - |", end=" ")
    for j in range(10):
        print(array_10x10[i][j], end=" ")
    print("|")
print("     ", end="")
for _ in range(23):
    print("-", end="")
print()
print("     ", end="")
for i in range(11):
    print(i, end=" ")