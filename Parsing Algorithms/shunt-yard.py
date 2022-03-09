from collections import deque
 
# Generates tokens from expressions
def tokenise(expr):
  num = ""
  ignore = " "
  tokens = []
  chars = list(expr)
  for i in range(0, len(chars)):
    if chars[i].isdigit():
      num += chars[i]
    #In the case of the last token being a number
      if(i==len(chars)-1):
        tokens.append(num)
    else:
      if len(num) > 0:
        tokens.append(num)
      num = ""
      if (chars[i] not in ignore):
        tokens.append(chars[i])
  return tokens


def precedence(op):
  if op in "/*":
    return 2
  elif op in "+-":
    return 1
  elif op in "^":
    return 3

# Transforms list of tokens into RPN/Post-fix notation
def gen_rpn(tokens):
  op_stack = deque()
  expr = []
  for i in range(0,len(tokens)):
    if tokens[i].isdigit():
      expr.append(tokens[i])
    else:
      if tokens[i] == "(":
        op_stack.append(tokens[i])
      else:
        if (len(op_stack)>0):
          if tokens[i] == ")":
            popped = ""
            while (popped != "("):
              popped = op_stack.pop()
              if popped == "(":
                break
              else:
                expr.append(popped)
          else:
            op = op_stack.pop()
            if op == "(":
              op_stack.append(op)
              op_stack.append(tokens[i])
            else:
              p1 = precedence(op)
              p2 = precedence(tokens[i])
              if p2 > p1:
                op_stack.append(op)
                op_stack.append(tokens[i])
              else:
                expr.append(op)
                op_stack.append(tokens[i])
        else:
          op_stack.append(tokens[i])
    #If we're at the end pop everything from the operator stack
    if i == (len(tokens)-1):
      while (len(op_stack)> 0):
        expr.append(op_stack.pop())
  return expr

def syntax_checker(tokens):
  # two consecutive numbers with no op in between
  # two consecutive operators
  # Brackets checker close and open needs to match () (()) is okay but (() is not
  brackets = deque()
  op = "/+*-^"
  valid = True
  if len(tokens) in [0,1]:
    valid = False
  else:
    for i in range(0, len(tokens)-1):
      # Consecutive num/op check
      invalid = (not tokens[i].isdigit()) and (not tokens[i] in op) and (not tokens[i] in "()")
      consecutive = (tokens[i+1] in op and tokens[i] in op) or (tokens[i+1].isdigit() and tokens[i].isdigit())
      if consecutive or invalid:
        valid = False
        break
  #Bracket checker
  others = []
  for i in range(0,len(tokens)):
    if tokens[i] in "(":
      brackets.append(tokens[i])
    elif tokens[i] == ")":
      if len(brackets) > 0:
        brackets.pop()
      else:
        valid = False
    else:
      others.append(tokens[i])
  if len(brackets) > 0 or len(others) == 0:
    valid = False
  return valid

def eval_op(n1,n2,op):
  n1 = int(n1)
  n2 = int(n2)
  if op == "+":
    return n1+n2
  elif op == "-":
    return n1-n2
  elif op == "*":
    return n1*n2
  elif op == "/":
    return n1/n2
  elif op == "^":
    return n1**n2

def eval_rpn(rpn):
  num_stack = deque()
  for i in rpn:
    if i.isdigit():
      num_stack.append(i)
    else:
      num1 = num_stack.pop()
      num2 = num_stack.pop()
      num_stack.append(eval_op(num2,num1,i)) 
  return num_stack.pop()
  
def main():
  expr = input("What operation would you like to do: ")
  while expr != "q":
    tokens = tokenise(expr)
    if syntax_checker(tokens):
      rpn = gen_rpn(tokens)
      print(eval_rpn(rpn))
    else:
      print("Invalid Expression")
    expr = input("What operation would you like to do: ")


if __name__ == "__main__":
  main()
