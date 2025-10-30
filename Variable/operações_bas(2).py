# Taken from mission Variable: Declaration and Value Setting
import operator as op
# 1. Declaring variable and setting their values
cyborgs = 10
# write your code here
robots=2
droids= 5
# 2. Setting values for variables in a single line
# write your code here
robots,droids = 2, 5
# 3. Declaring with type annotation
cyborgs: int = 10
# write your code here
robots:int = 2 
droids:int = 5
multi:int = None
add:int = None


# 1. Declaring new variables for sum and product and setting their values to expressions
# write your code here
add= op.add(droids,robots)
print(add)
multi= op.mul(robots, droids)
print(multi)