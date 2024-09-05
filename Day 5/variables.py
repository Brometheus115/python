'''Rules for variales
    variabels cant start with a number
    it can only start with letter and an underscore
    asides from the first character or the variabel,it can contain any other symbol
    try to avoid , $
    stick to numbers, letters and underscores
    variables in python are case sensetive'''
    
my_name = "Alice"
My_name = "Bob"
_my_name = "Jim"
           
age = 120
Age = 190
print (age, Age)

COUNTRY = "Germany" #all caps means constant, dont change aright?
print(COUNTRY)
COUNTRY= 78 #python doesnt care, its up to the devs
print(COUNTRY)
#integers, string,float, list
#dictionary
# build class
class Constant:
    #define your own class with specific rules
    DATE_OF_BIRTH = "1996-05-11" #DoB shouldnt change
                                 #so make it a constant for others to see

    
    
    