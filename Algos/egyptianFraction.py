"""
Greedy Algorithm for Egyptian Fraction
Every positive fraction can be represented as sum of unique unit fractions. A fraction is unit fraction 
if numerator is 1 and denominator is a positive integer, for example 1/3 is a unit fraction. Such a 
representation is called Egyptian Fraction as it was used by ancient Egyptians.

Following are few examples:

Egyptian Fraction Representation of 2/3 is 1/2 + 1/6
Egyptian Fraction Representation of 6/14 is 1/3 + 1/11 + 1/231
Egyptian Fraction Representation of 12/13 is 1/2 + 1/3 + 1/12 + 1/156
We can generate Egyptian Fractions using Greedy Algorithm. For a given number of the form ‘nr/dr’ where dr > nr, 
first find the greatest possible unit fraction, then recur for the remaining part. For example, consider 6/14, 
we first find ceiling of 14/6, i.e., 3. So the first unit fraction becomes 1/3, then recur for (6/14 – 1/3) i.e., 
4/42.
"""
import math

def egyptianFraction(nr, dr):
    """params
       nr  numerator
       dr  denominator
    """
    res = []
    while nr != 0:
        x = math.ceil(dr/nr)
        res.append(x)
        nr = nr*x - dr
        dr = dr*x
    
    for i in range(len(res)):
        if i != len(res) - 1:
            print('1/{} +'.format(res[i]), end=' ')
        else:
            print('1/{}'.format(res[i]), end='\n')

if __name__ == '__main__':
    egyptianFraction(6, 14)
    egyptianFraction(12, 13)
    egyptianFraction(2, 3)
    egyptianFraction(5, 6)
