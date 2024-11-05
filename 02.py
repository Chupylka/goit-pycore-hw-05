import re
from typing import Callable

def generator_numbers(text: str):
    numbers = re.findall(r'\b\d+\.\d+\b|\b\d+\b', text)
    for number in numbers:
        yield float(number) 

def sum_profit(text: str, func: Callable) -> float:
    return sum(func(text))
text = "The total income of the employee consists of several parts: 1000.01 as the main income, supplemented by additional income of 27.45 and 324.00 dollars."
total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income:.2f}")