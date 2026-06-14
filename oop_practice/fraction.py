class Fraction:

    def __init__(self,n,d):
        self.numerator = n
        self.denominator = d

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    def __add__(self,other):
        numer = self.numerator * other.denominator + other.numerator * self.denominator
        deno = self.denominator * other.denominator
        return Fraction(numer, deno) # create objec and return to temp variable
        
    def __sub__(self,other):
        numer = self.numerator * other.denominator - other.numerator * self.denominator
        deno = self.denominator * other.denominator
        return Fraction(numer, deno)
    
    
    def __mul__(self, other):
        numer = self.numerator * other.numerator
        deno = self.denominator * other.denominator
        return Fraction(numer, deno)
    
    def __truediv__(self, other):
        numer = self.numerator * other.denominator
        deno = self.denominator * other.numerator
        return Fraction(numer, deno) 
           
x = Fraction(2,3)
y = Fraction(1,2)
print(x + y) # in come case python create tem reference variable to access 
print(x - y)# all this occurs in backhend temp = x+y and print(tem)
print(x * y)
print(x / y)

