from package.math import *
from package.subpackage.mult import multiply

print(multiply(3, 4))  # This will call the multiply function from the subpackage
print(add(5, 6))  # This will call the add function from the math module