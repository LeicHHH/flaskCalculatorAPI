import math
import random
import string
import requests

class OperationService:
    @staticmethod
    def perform_operation(operation_type, amount):
        if operation_type == 'addition':
            return OperationService.addition(amount[0], amount[1])
        elif operation_type == 'subtraction':
            return OperationService.subtraction(amount[0], amount[1])
        elif operation_type == 'multiplication':
            return OperationService.multiplication(amount[0], amount[1])
        elif operation_type == 'division':
            return OperationService.division(amount[0], amount[1])
        elif operation_type == 'square_root':
            return OperationService.square_root(amount[0])
        elif operation_type == 'random_string':
            return OperationService.generate_random_string(amount[0])

    @staticmethod
    def addition(amount1, amount2):
        return amount1 + amount2

    @staticmethod
    def subtraction(amount1, amount2):
        return amount1 - amount2

    @staticmethod
    def multiplication(amount1, amount2):
        return amount1 * amount2

    @staticmethod
    def division(amount1, amount2):
        if amount2 == 0:
            raise ValueError('Division by zero.')
        return amount1 / amount2

    @staticmethod
    def square_root(amount):
        return math.sqrt(amount)

    @staticmethod
    def generate_random_string(length):
        response = requests.get(f'https://www.random.org/integers/?num={length}&min=0&max=61&col=1&base=10&format=plain&rnd=new')
        integers = list(map(int, response.text.strip().split('\n')))
    
        allowed_characters = string.ascii_letters + string.digits
        return ''.join(allowed_characters[i] for i in integers)
