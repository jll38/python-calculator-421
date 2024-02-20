class operations:
    @staticmethod
    def add(a: int | float, b: int | float) -> int | float:
        return a + b

    @staticmethod
    def subtract(a: int | float, b: int | float) -> int | float:
        return a - b

    @staticmethod
    def mutliply(a: int | float, b: int | float) -> int | float:
            return a * b


    @staticmethod
    def divide(a: int | float, b: int | float) -> int | float:
        if(b == 0): 
             raise ValueError("Cannot divide by zero")
        return a / b
    
    @staticmethod
    def floorDivide(a: int | float, b: int()) -> int:
        if(b == 0): 
             raise ValueError("Cannot divide by zero")
        return a//b

    @staticmethod
    def modulo(a: int, b: int) -> int:
        if(b == 0): 
             raise ValueError("Cannot modulo with zero")
        return a % b
