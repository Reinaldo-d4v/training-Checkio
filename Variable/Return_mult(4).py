import operator as op
def mult_two(a: int, b: int) -> int:
    # your code here
    multi=op.mul(a,b)
    return multi
print(mult_two(3,2))

print("Example")
print(mult_two(1, 2))

assert mult_two(3, 2) == 6
assert mult_two(0, 1) == 0

print("The first mission is done! Click 'Check' to earn cool rewards!")

 
