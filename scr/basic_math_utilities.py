"""
to use path to C:\stuff\code\python\packages\pythonSamples\ in the cmd line

cd C:\stuff\code\python\packages\pythonSamples\
then
pytest -v > tests.log

tests.log should write to C:\stuff\code\python\packages\pythonSamples\tests.log
"""

class BasicMathUtilities():
    
    def __init__(self):
        pass

    @ staticmethod
    def add(value_1, value_2):
        return value_1 + value_2

    @ staticmethod
    def divide(value_1, value_2):
        try:  
            return value_1 / value_2
        except ZeroDivisionError:  
            raise ZeroDivisionError("Division by zero") 
        