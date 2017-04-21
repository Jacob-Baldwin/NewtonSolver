from sympy import *

MAX_ITERATIONS = 1000
CLOSENESS_THRESH = 0.000001
DECIMAL_PRECISION = 6

def loadConfig():

    #Loads parameters from config.ini

    config_file = open('config.ini','r')
    MAX_ITERATIONS = config_file.readline().split()[1]
    CLOSENESS_THRESH = config_file.readline().split()[1]
    DECIMAL_PRECISION = config_file.readline().split()[1]

def getStartingInput():

    #Prompts the user for an equation and a point for x0.
    #Will also check that the equation can be interpreted by sympy and if not will reprompt the user
    #Returns a sympy expression and a float

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

    #Evaluates the value of the derivative of a given equation at the given point.
    #Expects a sympy expression and a float point as input
    #Returns a float.

    x = symbols('x')
    differentiated_equation = diff(equation,x)
    differentiated_equation = differentiated_equation.subs(x, point)
    return differentiated_equation.evalf()

def evaluateEquation(equation,point):

    #Evaluates an equation at a given point.
    #Expects a sympy expression and a float point
    #Returns a float

    x = symbols('x')
    equation = equation.subs(x, point)
    return equation.evalf()

def evaluateSingleIteration(equation,point):

    #Evaluates a single iteration of Newton's Method. Using the formula x1 = x0 - f(x0)/f'(x0)
    #Expects a sympy expression and a float point
    #Returns a float point x1

    x = symbols('x')
    fx = evaluateEquation(equation,point)
    fpx = evaluateDerivative(equation,point)

    x0 = point
    x1 = x0 - (fx/fpx)

    return (x1)

def newtonsMethod(equation, starting_point):

    #Evaluates Newton's Method of the given equation starting at starting_point up until MAX_ITERATIONS.
    #Expects a sympy expression and a float starting_point
    #Returns the x value of the solution. If MAX_ITERATIONS is reached will return NONE.

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

        #Instead of if x1 == x0 we measure the difference of x1 and x0 and if they are within CLOSENESS_THRESH we consider them equal.
        #This is because in some cases the two numbers will keep converging closer and closer without ever being equal.
        #Resulting in the function continuing to calculate until MAX_ITERATIONS is reached.
        if (abs(x1 - x0) < CLOSENESS_THRESH):
            return x1
        if (number_of_iterations >= MAX_ITERATIONS):
            print("No Solution within", number_of_iterations, "iterations.")
            return

        x0 = x1
        number_of_iterations = number_of_iterations + 1

def main():
    loadConfig()
    equation, starting_point = getStartingInput()

    try:
        solution = newtonsMethod(equation,starting_point)
        print("Solution:")

        #First tries to print the number rounded to DECIMAL_PRECISION.
        #If the number can't be rounded (for example if newtonsMethod returned an irrational number) it will just print the unrounded value.
        try:
            print("x =", round(solution, DECIMAL_PRECISION))
        except:
            print("x =", solution)

    except:
        print("Error")
        solution = "Error"

main()
