##########################EX 1##############################
class Stack():
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def top(self):
        return self.stack[-1]

    def pop(self):
        res = self.top()
        self.stack = self.stack[:-1]
        return res

    def isEmpty(self):
        return len(self.stack) == 0
    
class CalculatorEngine():
    def __init__(self):
        self.dataStack = Stack()
    
    def pushOperand(self, val):
        self.dataStack.push(val)
    
    def currentOperand(self):
        return self.dataStack.top()
    
    def performBinary(self, func):
        right = self.dataStack.pop()
        left = self.dataStack.pop()
        self.dataStack.push(func(left,right))
    
    def doAdd(self):
        self.performBinary(lambda x,y:x+y)
        
    def doSub(self):
        self.performBinary(lambda x,y:x-y)
        
    def doMul(self):
        self.performBinary(lambda x,y:x*y)
        
    def doDiv(self):
        self.performBinary(lambda x,y:x/y)
    
    
    def doTextOp(self,op):
        if(op == '+'):
            self.doAdd()
        elif(op == '-'):
            self.doSub()
        elif(op == '*'):
            self.doMul()
        elif(op == '/'):
            self.doDiv()
    
class RPNCalculator():
    def __init__(self):
        self.cal = CalculatorEngine()
    
    def eval(self,line):
        words = line.split()
        error = False
        for item in words:
            if item in '+-*/':
                self.cal.doTextOp(item)
            elif item == '%':
                try:
                    self.cal.performBinary(lambda x,y:x%y)
                except ZeroDivisionError:
                    print('divide by 0')
                    error = True
                    break
            else:
                self.cal.pushOperand(int(item))   
        if error != True:
            return self.cal.currentOperand()
    
    def run(self):
        while True:
            line = input("type an expression: ")
            if len(line == 0):
                break
            print(self.eval(line))
    
#cal = RPNCalculator()
#x = cal.eval('6 5 %')
##########################EX 1##############################

##########################EX 2##############################
a = range(1,11)
res1 = list(map(lambda x: x*x, a))
res2 = list(map(lambda x: x+1, a))
res3 = [x for x in filter(lambda x: x <= 5, a)]
res4 = [x for x in filter(lambda x: x % 2 == 0, list(map(lambda x: x*x, a)))]  
##########################EX 2##############################    
