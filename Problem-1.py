class Calc:
    def __init__(self):
        pass
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        if b==0:
            return "Error: Division by Zero"
        else:
            return a/b
    def calculator(self,a,b,operation_type):
        if operation_type=="Addition":
            return self.add(a,b)
        elif operation_type == "Subtraction":
            return self.sub(a, b)
        elif operation_type == "Multiplication":
            return self.mul(a, b)
        elif operation_type == "Division":
            return self.div(a, b)
        else:
            return "Invalid Operation Type choose from Addition,Subtraction,Multiplication,Division"
if __name__=="__main__":
    calc=Calc()
    Testcase=int(input("Enter No of Testcase:"))
    for i in range(Testcase):
        a=float(input())
        b=float(input())
        op=input()
        result=calc.calculator(a,b,op)
        print(f"{a} {op} {b} = {result}")
