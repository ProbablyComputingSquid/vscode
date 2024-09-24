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
for x in range(10):
    #print('for x = ', i, ', y = ', evaluate(equation, i))
    y = int(evaluate(equation, x))
    y_last_x = int(evaluate(equation, x-1))
    if (y < 10 and y >= 0):
        array_10x10[y][x] = "*"
        if (abs(y_last_x-y) > 1):
            if (y > y_last_x):
                for i in range(min(y, y_last_x + 1), max(y, y_last_x + 1)):
                    array_10x10[i][x] = "*"
            else:
                for i in range(min(y, y_last_x), max(y, y_last_x)):
                    array_10x10[i][x] = "*"
        


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