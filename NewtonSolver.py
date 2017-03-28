from sympy import *

MAX_ITERATIONS = 3000
CLOSENESS_THRESH = 0.00000001

def getStartingInput():
    print("Please enter the equation to evaluate (example: 3*x**2 + 4*x + 1/2): ")

    prompt_for_equation = True

    while prompt_for_equation:
        user_equation = input()
        try:
            user_equation = sympify(user_equation)
            prompt_for_equation = False
        except:
            print ("Invalid input, please enter the equation again:")


    print("Please enter a point to start looking for a root:")
    starting_point = input()
    starting_point = float(starting_point)

    return user_equation, starting_point

def evaluateDerivative(equation,point):
    x = symbols('x')
    differentiated_equation = diff(equation,x)
    differentiated_equation = differentiated_equation.subs(x, point)
    return differentiated_equation.evalf()

def evaluateEquation(equation,point):
    x = symbols('x')
    equation = equation.subs(x, point)
    return equation.evalf()

def evaluateSingleIteration(equation,point):
    x = symbols('x')
    fx = evaluateEquation(equation,point)
    fpx = evaluateDerivative(equation,point)

    x0 = point
    x1 = x0 - (fx/fpx)

    return (x1)

def newtonsMethod(equation, starting_point):
    x0 = starting_point
    stop = False
    number_of_iterations = 0

    print()
    print("x0 =", x0)
    print()

    while (stop == False):
        x1 = evaluateSingleIteration(equation,x0)
        print("x" + str(number_of_iterations + 1), "=", x1)
        print()

        if (abs(x1 - x0) < CLOSENESS_THRESH):
            return x1
        if (number_of_iterations >= MAX_ITERATIONS):
            print("No Solution within", number_of_iterations, "iterations.")
            return

        x0 = x1
        number_of_iterations = number_of_iterations + 1

def main():
    equation, starting_point = getStartingInput()

    try:
        solution = newtonsMethod(equation,starting_point)
        print("Solution:")
        try:
            print("x =", round(solution, 6))
        except:
            print("x =", solution)

    except:
        print("Error")
        solution = "Error"



main()
