
"""
Transfer fahrenheit to centigrade
F = 1.8C + 32


Author: Ray
Date: 2019.08.18

"""

F = float((input('input the centigrade:')))
C = (F - 32) / 1.8
print('%.1fF = %.1fC' % (F, C))

