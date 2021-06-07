# UNDERSTANDING CONCEPT OF "self" KEYWORD and __init__()

print("Class ValueA Illustration : (with __init__())")
class ValueA:
    # Here , c and d can be accessed outside class using object name
    c = 50
    global d
    d = 60
    def __init__(self,a,b):
        self.a=a
        self.b=b
    # Here , passing "self" in function as an argument is compulsory
    # Here , Since we have self for accessing a and b therefore it is mandatory to pass "self" in inner_function()
    # def inner_function(): --> GIVES ERROR
    def inner_function1(self):
        c=30
        # Here, since c is class variable and not instance variable therefore we cannot use "self" to access class variables
        # print("Value of a : ",self.a,"Value of b : ",self.b,"Value of c : ",self.c) --> GIVES ERROR
        print("inner_function1() : Value of a : ", self.a," , Value of b : ", self.b,"and Value of c : ",c)
    def inner_function2(self):
        c=40
        # Here, since a and b are instance variables therefore we have to use "self" to access class variables
        # print("Value of a : ", a," , Value of b : ",b,"and Value of c : ",c) --> GIVES ERROR
        print("inner_function2() : Value of c : ",c)
    def inner_function3(self):
        print("inner_function3() : inner_function2() called")
    # def inner_function4(self):
        # Here, d cannot be accessed
        # print("Value of d : ",d) --> GIVES ERROR NameError


oA=ValueA(10,20)
oA.inner_function1()
oA.inner_function2()
oA.inner_function3()

# Here , "c" cannot be accessed outside the scope of function in a class without object name
# print("Value of c : ",c) --> GIVES NameError

# Here , "c" can be accessed  outside the scope of function in a class only using object name
print("Value of c : ",oA.c)

# Here , "d" is global variable so can be accessed outside the scope of class too without using object name
print("Value of d : ",d)
#print("Value of c : ",self.c) --> Since , "c" is not an instance variable so no need of "self"
print()

print("Class ValueB Illustration : (without __init__())")
class ValueB :
    c = 50
    def inner_function1(self):
        c=30
        print("inner_function1() : Value of c : ",c)
    def inner_function2(self):
        print("inner_function2() : called")
oB = ValueB()
oB.inner_function1()
oB.inner_function2()
print()

# Always remember , prefernce is gievn to the value given at function call over the value given at function definition
print("Class ValueC Illustration : (using default values)")
class ValueC :
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def inner_function1(self,c=90):
        print("inner_function1() : Value of a : ", self.a, " , Value of b : ", self.b," , Value of c : ", c)

    # Here, execution of program terminates as value of c is not given at function call and difinition both yet printed when function called
    #def inner_function(self,c):
        #print("inner_function() : Value of a : ", self.a, " , Value of b : ", self.b," , Value of c : ", c)

    def inner_function2(self,c=30):
        print("inner_function2() : Value of a : ", self.a, " , Value of b : ", self.b," , Value of c : ", c)

    def inner_function3(self,a=100,b=200):
        print("inner_function3() : Value of a : ", a, " , Value of b : ",b)
        # when we use "self" keyword , values passed in function call or definition are all neglected
        # only values passed during object creation are accessed always
        print("inner_function3() : Value of a : ", self.a, " , Value of b : ", self.b)

oC = ValueC(10,20)
oC.inner_function1()             # variable given at function definition can be used within function
oC.inner_function2()             # when no value of "c" is passed here , so the value given at function definition is used
oC.inner_function2(300)          # value passed at function call is preferred over value given at function definition
oC.inner_function3()
oC.inner_function3(15,25)
print()

print("Function outside classes Illustration :")
# Here , "self" is not passed in function as this function is not within class
# Here , "self" is a parameter of functions which are within class
# def inner_function4(self): --> GIVES TypeError
def outer_function():
    print("outside_function() : called ")
outer_function()
print()
