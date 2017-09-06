"""
Problem:
Write a simple interpreter which understands "+", "-", and "*" operations. 
Apply the operations in order using command/arg pairs starting with the initial value of `value`. 
If you encounter an unknown command, 
return -1. 
interpret(1, ["+"], [1]) → 2 
interpret(4, ["-"], [2]) → 2 
interpret(1, ["+", "*"], [1, 3]) → 6
"""

def interpret(value, commands, args):
  result = value
  for i,j in enumerate(commands):
    if j=="+":
      result = result+args[i]
    elif j=="-":
      result = result-args[i]
    elif j=="*":
      result = result*args[i]
    else:
      return -1
  return result
