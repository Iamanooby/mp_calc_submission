

def mergesort(array, byfunc=None):
  len_array = len(array)
  if len_array<=1:
    pass
  else:
    arrayL_len  = len_array//2
    arrayR_len  = len_array- arrayL_len
    arrayL = array[:arrayL_len]
    arrayR = array[arrayL_len:]
    mergesort(arrayL,byfunc)
    mergesort(arrayR,byfunc)
    i = 0
    j = 0
    k = 0

    while i< arrayL_len and j < arrayR_len:
      left_array_element = byfunc(arrayL[i])
      right_array_element = byfunc(arrayR[j])
      if left_array_element<=right_array_element:
        array[k] = arrayL[i]
        k+=1
        i+=1
      else:
        array[k] = arrayR[j]
        k+=1
        j+=1
  
    if i< arrayL_len: array[k:] = arrayL[i:]

    if j< arrayR_len: array[k:] = arrayR[j:]

  return array

    

    

    

    

class Stack:
  def __init__(self):
    self._items = []
  
  def push(self,char):
    self._items.append(char)
  
  def pop(self):
    return self._items.pop()

  def peek(self):
    return self._items[-1]


class EvaluateExpression:
  valid_char = '0123456789+-*/() '
  def __init__(self, string=""):
    self.expression = string

  @property
  def expression(self):
    return self._expression

  @expression.setter
  def expression(self, new_expr):
    valid_exp = True#sets to false as long as a single character does not belong
    for char in new_expr:
      valid_exp = valid_exp and char in self.valid_char
    if valid_exp:
      self._expression = new_expr
    else:
      self._expression = ""

  def insert_space(self):
    spaced_str = ""
    for i in self._expression:
      if i in "+-*/()":
        spaced_str += " " + i + " "
      else:
        spaced_str += i
    return spaced_str

  def process_operator(self, operand_stack, operator_stack):
    right_operand = operand_stack.pop()
    left_operand = operand_stack.pop()
    operator = operator_stack.pop()
    if operator == "+":
      operand_stack.push(left_operand+right_operand)
    elif operator == "-":
      operand_stack.push(left_operand-right_operand)
    elif operator == "*":
      operand_stack.push(left_operand*right_operand)      
    elif operator == "/":
      operand_stack.push(left_operand//right_operand)

      
  def evaluate(self):

    #if plus or minus, compute everything before
    #if closed bracket, compute everything before
    #if times or divide, then let it compound untill you hit either of the above

    operand_stack = Stack()
    operator_stack = Stack()
    
    expression = self.insert_space()
    tokens = expression.split()
    try:#catch errors and return "invalid expression" in the except block
        for index,char in enumerate(tokens):


          if char.isnumeric():#check if its a value. if it is, push it into the stack
            operand_stack.push(int(char))
          elif char in "+-":#check if its an operator. if it is call the process operator function. 
            while(len(operator_stack._items) > 0 and operator_stack.peek() not in "()" ):#check for bracket using PEMDAS logic
              self.process_operator(operand_stack, operator_stack)
            operator_stack.push(char)#push final result into stack
          elif char in "*/":#check if its an operator. if it is call the process operator function. 
            while(len(operator_stack._items) > 0 and operator_stack.peek() in "*/"):#check if its still an expression
              self.process_operator(operand_stack, operator_stack)#keep calling process_operator until its not an */ operator anymore
            operator_stack.push(char)#push final result into stack      
          elif char == "(":#check if its a bracket, if it is push the bracket into stack
            operator_stack.push(char)
          elif char == ")":
            while not(operator_stack.peek() == "("):#if its a close bracket, evaluate everything inside the bracket until the stack reaches an open bracket
              self.process_operator( operand_stack, operator_stack)
            operator_stack.pop()# to remove ( "("
          # print(char, operand_stack._items, operator_stack._items)


        while (len(operator_stack._items) > 0):
          self.process_operator(operand_stack, operator_stack)

        return operand_stack.peek()
    except:#some expression has caused the code to break; invalid expression gets returned instead
        return "invalid expression"



def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





