# class Rational:
#     '''Documentation'''
#     def __init__(self, numerator, denominator):
#         '''Initializer'''
#         if denominator == 0:
#             raise ValueError("Denominator cannot be zero.")
#         self.numerator = numerator
#         self.denominator = denominator
#         self._mixed_form = None

#     @property
#     def mixed_form(self):
#         '''Getter'''
#         if self.numerator == 0:
#             return '0'
#         counter = 0
#         numerator = abs(self.numerator)
#         denominator = abs(self.denominator)
#         while numerator >= denominator:
#             numerator -= denominator
#             counter += 1
#         sign = '-' if (self.numerator < 0) != (self.denominator < 0) else ''
#         return f'{sign}{counter} {numerator}/{denominator}' if counter > 0 else f'{sign}{numerator}/{denominator}'
    
#     @mixed_form.setter
#     def mixed_form(self, value):
#         '''Setter for mixed form'''
#         if ' ' in value:
#             integer_part, fraction = value.split()
#             numerator, denominator = map(int, fraction.split('/'))
#             integer_part = int(integer_part)
#             sign = -1 if integer_part < 0 else 1
#             self.numerator = sign * (abs(integer_part) * denominator + numerator)
#             self.denominator = denominator
#         else:
#             numerator, denominator = map(int, value.split('/'))
#             self.numerator = numerator
#             self.denominator = denominator
#         # self.reduce()

#     def __str__(self):
#         '''Returns a string representation'''
#         if self.numerator == 0:
#             return f'0/{abs(self.denominator)}'
#         sign = '-' if self.numerator * self.denominator < 0 else ''
#         return f"{sign}{abs(self.numerator)}/{abs(self.denominator)}"
#         # if self.denominator <= 0:
#         #     if self.numerator == 0:
#         #         return f'0/{abs(self.denominator)}'
#         #     return f'-{self.numerator}/{abs(self.denominator)}'
#         # return f'{self.numerator}/{self.denominator}'
    
#     def reduce(self):
#         '''Reduces the rational number'''
#         if self.numerator == 0:
#             return Rational(0, 1)
#         dilnyky = []
#         for i in range(1, min(abs(self.numerator), abs(self.denominator)) + 1):
#             if self.denominator % i == 0 and self.numerator % i == 0:
#                 dilnyky.append(i)
#         common_d = max(dilnyky)
#         self.numerator = self.numerator // common_d
#         self.denominator = self.denominator // common_d
#         return self

#     def __add__(self, other):
#         '''Adds'''
#         common_denominator = self.denominator * other.denominator
#         numerator_sum = (self.numerator * other.denominator) + (other.numerator * self.denominator)
#         return Rational(numerator_sum, common_denominator).reduce()

#     def __sub__(self, other):
#         '''Subtracts'''
#         common_denominator = self.denominator * other.denominator
#         numerator_sum = (self.numerator * other.denominator) - (other.numerator * self.denominator)
#         return Rational(numerator_sum, common_denominator).reduce()

#     def __mul__(self, other):
#         '''Multiplies'''
#         num = self.numerator * other.numerator
#         den = self.denominator * other.denominator
#         return Rational(num, den).reduce()

#     def __truediv__(self, other):
#         '''Divides //'''
#         num = self.numerator * other.denominator
#         den = self.denominator * other.numerator
#         if den == 0:
#             raise ValueError("Denominator cannot be zero in division.")
#         return Rational(num, den).reduce()

#     def __eq__(self, other):
#         '''Checks equality between two rational numbers'''
#         return self.reduce().numerator == other.reduce().numerator and self.reduce().denominator == other.reduce().denominator

#     def __lt__(self, other):
#         '''<'''
#         return (self.reduce().numerator * other.reduce().denominator) < (self.reduce().denominator * other.reduce().numerator)

#     def __le__(self, other):
#         '''<='''
#         return (self.reduce().numerator * other.reduce().denominator) <= (self.reduce().denominator * other.reduce().numerator)


# def test_rational():
#     """Testing class Rational ..."""
#     # This is an implementation of a Rational numbers
#     # that consist of 2 parts - nominator and denominator.
#     # You can imagine this Ratinal numbers as fractions
#     # like 3/4
#     rational1 = Rational(1, 4)
#     assert rational1.numerator == 1
#     assert rational1.denominator == 4
#     assert isinstance(rational1, Rational)
#     assert str(rational1) == "1/4"

#     try:
#         rational2 = Rational(1, 0)
#     except ValueError as e:
#         assert f'{e}' == "Denominator cannot be zero."

#     rational2 = Rational(2, 4)
#     assert rational2.numerator == 2
#     assert rational2.denominator == 4
#     assert isinstance(rational2, Rational)
#     assert str(rational2) == "2/4"
#     rational2 = rational2.reduce()
#     assert str(rational2) == "1/2"

#     # here you can add two numbers
#     rational2 = Rational(2, 5)
#     assert str(rational1 + rational2) == "13/20", str(rational1 + rational2)

#     # here is a substraction
#     assert str(rational1 - rational2) == "-3/20"

#     # multiplication
#     assert str(rational1 * rational2) == "1/10", str(rational1 * rational2)

#     # division
#     assert str(rational1 / rational2) == "5/8"

#     assert str(rational1 / rational2*rational1-rational1) == "-3/32"

#     rational3 = Rational(2, 8)
#     assert str(rational3) == "2/8"

#     assert rational1 == rational3

#     assert rational1 < rational2

#     assert rational1 <= rational2

#     assert rational1 <= rational3

#     rational3 = Rational(2, -8)
#     assert str(rational3) == "-2/8"

#     rational4 = Rational(10, 8)
#     assert str(rational4) == "10/8"
#     assert rational4.mixed_form == "1 2/8", rational4.mixed_form

#     rational4.mixed_form = '2 3/5'
#     assert str(rational4) == '13/5'
#     assert isinstance(rational4, Rational)

#     rational4.mixed_form = '3/5'
#     assert str(rational4) == '3/5'

#     rational5 = Rational(0, -4)
#     assert rational5.mixed_form == '0', rational5.mixed_form
#     assert str(rational5) == '0/4'
#     assert str(rational5.reduce()) == '0/1'

#     rational6 = Rational(10, -8)
#     assert str(rational6) == "-10/8"
#     assert rational6.mixed_form == "-1 2/8"

#     rational7 = Rational(-10, 8)
#     assert str(rational7) == "-10/8"
#     assert rational7.mixed_form == "-1 2/8"

#     rational4.mixed_form = "-1 2/8"
#     assert str(rational4) == '-10/8', str(rational4)
#     assert rational4.numerator == -10
#     assert rational4.denominator == 8
#     assert isinstance(rational4, Rational)

#     print("Done!")


# if __name__ == '__main__':
#     test_rational()



# class Rational:
#     '''Documentation'''
#     def __init__(self, numerator, denominator):
#         '''Initializer'''
#         if denominator == 0:
#             raise ValueError("Denominator cannot be zero.")
#         self.numerator = numerator
#         self.denominator = denominator
#         self._mixed_form = None

#     @property
#     def mixed_form(self):
#         '''Getter'''
#         if self.numerator == 0:
#             return '0'
#         counter = 0
#         numerator = abs(self.numerator)
#         denominator = abs(self.denominator)
#         while numerator >= denominator:
#             numerator -= denominator
#             counter += 1
#         sign = '-' if (self.numerator < 0) != (self.denominator < 0) else ''
#         return f'{sign}{counter} {numerator}/{denominator}' if counter > 0 else\
# f'{sign}{numerator}/{denominator}'

#     @mixed_form.setter
#     def mixed_form(self, value):
#         '''Setter for mixed form'''
#         if ' ' in value:
#             integer_part, fraction = value.split()
#             numerator, denominator = map(int, fraction.split('/'))
#             integer_part = int(integer_part)
#             sign = -1 if integer_part < 0 else 1
#             self.numerator = sign * (abs(integer_part) * denominator + numerator)
#             self.denominator = denominator
#         else:
#             numerator, denominator = map(int, value.split('/'))
#             self.numerator = numerator
#             self.denominator = denominator
#         # self.reduce()

#     def __str__(self):
#         '''Returns a string representation'''
#         if self.numerator == 0:
#             return f'0/{abs(self.denominator)}'
#         sign = '-' if self.numerator * self.denominator < 0 else ''
#         return f"{sign}{abs(self.numerator)}/{abs(self.denominator)}"

#     def reduce(self):
#         '''Reduces the rational number'''
#         if self.numerator == 0:
#             return Rational(0, 1)
#         dilnyky = []
#         for i in range(1, min(abs(self.numerator), abs(self.denominator)) + 1):
#             if self.denominator % i == 0 and self.numerator % i == 0:
#                 dilnyky.append(i)
#         common_d = max(dilnyky)
#         self.numerator = self.numerator // common_d
#         self.denominator = self.denominator // common_d
#         return self

#     def __add__(self, other):
#         '''Adds'''
#         common_denominator = self.denominator * other.denominator
#         numerator_sum = (self.numerator * other.denominator) + (other.numerator * self.denominator)
#         return Rational(numerator_sum, common_denominator).reduce()

#     def __sub__(self, other):
#         '''Subtracts'''
#         common_denominator = self.denominator * other.denominator
#         numerator_sum = (self.numerator * other.denominator) - (other.numerator * self.denominator)
#         return Rational(numerator_sum, common_denominator).reduce()

#     def __mul__(self, other):
#         '''Multiplies'''
#         num = self.numerator * other.numerator
#         den = self.denominator * other.denominator
#         return Rational(num, den).reduce()

#     def __truediv__(self, other):
#         '''Divides //'''
#         num = self.numerator * other.denominator
#         den = self.denominator * other.numerator
#         if den == 0:
#             raise ValueError("Denominator cannot be zero.")
#         return Rational(num, den).reduce()

#     def __eq__(self, other):
#         '''Checks equality between two rational numbers'''
#         return self.reduce().numerator == other.reduce().numerator and \
# self.reduce().denominator == other.reduce().denominator

#     def __lt__(self, other):
#         '''<'''
#         return (self.reduce().numerator * other.reduce().denominator) <\
# (self.reduce().denominator * other.reduce().numerator)

#     def __le__(self, other):
#         '''<='''
#         return (self.reduce().numerator * other.reduce().denominator) <=\
# (self.reduce().denominator * other.reduce().numerator)



class Rational:
    '''
    A class to represent a rational number.
    
    Attributes:
    numerator (int): The numerator of the rational number.
    denominator (int): The denominator of the rational number.
    
    Methods:
    mixed_form: Returns the mixed fraction representation.
    reduce(): Reduces the fraction to its simplest form.
    
    Supported operations:
    - Addition (+)
    - Subtraction (-)
    - Multiplication (*)
    - Division (/)
    - Equality (==)
    - Less than (<)
    - Less than or equal to (<=)
    '''
    
    def __init__(self, numerator, denominator):
        '''
        Initializes a Rational number.
        
        >>> r = Rational(3, 4)
        >>> r.numerator, r.denominator
        (3, 4)
        >>> Rational(1, 0)  # Should raise an error
        Traceback (most recent call last):
        ValueError: Denominator cannot be zero.
        '''
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator

    @property
    def mixed_form(self):
        '''
        Returns the mixed fraction form of the rational number.
        
        >>> Rational(7, 2).mixed_form
        '3 1/2'
        >>> Rational(-7, 2).mixed_form
        '-3 1/2'
        >>> Rational(0, 5).mixed_form
        '0'
        '''
        if self.numerator == 0:
            return '0'
        counter = 0
        numerator = abs(self.numerator)
        denominator = abs(self.denominator)
        while numerator >= denominator:
            numerator -= denominator
            counter += 1
        sign = '-' if (self.numerator < 0) != (self.denominator < 0) else ''
        return f'{sign}{counter} {numerator}/{denominator}' if counter > 0 else f'{sign}{numerator}/{denominator}'

    def __str__(self):
        '''
        Returns a string representation of the rational number.
        
        >>> str(Rational(5, 3))
        '5/3'
        >>> str(Rational(-5, 3))
        '-5/3'
        >>> str(Rational(0, 3))
        '0/3'
        '''
        if self.numerator == 0:
            return f'0/{abs(self.denominator)}'
        sign = '-' if self.numerator * self.denominator < 0 else ''
        return f"{sign}{abs(self.numerator)}/{abs(self.denominator)}"
    
    def reduce(self):
        '''
        Reduces the rational number to its simplest form.
    
        '''
        if self.numerator == 0:
            return Rational(0, 1)
        from math import gcd
        common_d = gcd(self.numerator, self.denominator)
        return Rational(self.numerator // common_d, self.denominator // common_d)
    
    def __add__(self, other):
        '''
        Adds two rational numbers.
        
        '''
        common_denominator = self.denominator * other.denominator
        numerator_sum = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        return Rational(numerator_sum, common_denominator).reduce()

    def __sub__(self, other):
        '''
        Subtracts two rational numbers.

        '''
        common_denominator = self.denominator * other.denominator
        numerator_diff = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        return Rational(numerator_diff, common_denominator).reduce()
    
    def __mul__(self, other):
        '''
        Multiplies two rational numbers.
        
        '''
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator).reduce()
    def __truediv__(self, other):
        '''
        Divides two rational numbers.
        
        '''
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        return Rational(self.numerator * other.denominator, self.denominator * other.numerator).reduce()

    def __eq__(self, other):
        '''
        Checks equality between two rational numbers.
        
        >>> Rational(2, 4) == Rational(1, 2)
        True
        '''
        return self.reduce().numerator == other.reduce().numerator and self.reduce().denominator == other.reduce().denominator

    def __lt__(self, other):
        '''
        Checks if a rational number is less than another.
        
        >>> Rational(1, 3) < Rational(1, 2)
        True
        '''
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __le__(self, other):
        '''
        Checks if a rational number is less than or equal to another.
        
        >>> Rational(2, 3) <= Rational(2, 3)
        True
        '''
        return self.numerator * other.denominator <= self.denominator * other.numerator
if __name__ == '__main__':
    import doctest 
    print(doctest.testmod())