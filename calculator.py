def calculate(num1,num2,op):
    '''
    calculate(num1,num2,op) :
    num1--- integer value
    num2--- integer value
    op----- operator +,-,*,//
    '''
    if op == '+': return num1+num2
    elif op == '-': return num1-num2
    elif op == '//':
        try:
            return num1//num2
        except ZeroDivisionError:
            return "Cannot divide by zero"
    elif op == '*':
        return num1*num2
    else: 
        return "Unsupported operator"