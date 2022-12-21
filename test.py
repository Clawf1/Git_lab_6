import calc

print('File imported!')
assert calc.simple_calculator("2+2") == 4, "correct addition: should be 4"
assert calc.simple_calculator("2-2") == 0, "correct subtraction: should be 0"
assert calc.simple_calculator("2/2") == 1, "correct division: should be 1"
assert calc.simple_calculator("2*2") == 4, "correct multiplication: should be 4"
assert calc.simple_calculator("8//2") == 4, "correct DIV: should be 4"
assert calc.simple_calculator("2%2") == 0, "correct MOD: should be 0"
assert calc.simple_calculator("2+2*2") == 6, "support of operations priorities"
assert calc.simple_calculator("(2+2)*2") == 8, "support of brackets priorities"
assert calc.simple_calculator("10-15") == -5, "should support negative numbers"
assert calc.simple_calculator("0.1 + 0.2") - 0.3 <= 1 / (10 ** 8), "bad accuracy for float"
assert calc.simple_calculator("2+2 == 4") == True, "should support boolean"
assert calc.simple_calculator("0**0") == 1, "tricky exponentiation!"
assert calc.simple_calculator("import os") == 'ERR', "should be safe"
assert calc.simple_calculator("1/0") == 'ERR', "mustn't do unsupported operations"
assert calc.simple_calculator("1%0") == 'ERR', "mustn't do unsupported operations"
assert calc.simple_calculator("1//0") == 'ERR', "mustn't do unsupported operations"
assert calc.simple_calculator("temp = 10") == 'ERR', "mustn't support declaration"
assert calc.simple_calculator("equation = '2+2'") == 'ERR', "mustn't change local variables"
assert calc.simple_calculator("2**1024") == 2 ** 1024, "should support long numbers"
assert calc.simple_calculator("sum([2,3])") == 5, "should support built-in functions"
assert calc.simple_calculator("0 or 0") == 0, "should support boolean algebra: answer is 0"
assert calc.simple_calculator("1 and 0") == 0, "should support boolean algebra: answer is 0"
assert calc.simple_calculator("1 and 0 or 0") == 0

print('all tests passed!')
