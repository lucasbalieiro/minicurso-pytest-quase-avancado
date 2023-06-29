import sys

class CustomError(Exception):
    pass

class Calculator():
    def add(self, a, b):
        if a == 666:
            raise CustomError("Erro socorro!")
        
        sys.stderr.write("sem erros")
        print(f"adicao executada")
        return a + b
    
    def sub(self, a, b):
        return a - b
