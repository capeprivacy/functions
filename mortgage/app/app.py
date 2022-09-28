# Determine if someone is eligible for a mortgage
import json

MIN_DOWN_PERCENTAGE = 0.05
MIN_SALARY = 0.1

def mortgage(salary, amount, down):
    downPercentage = (100 * down) / amount
    salaryPercentage = (100 * salary) / amount
    if down > amount:
        return "You do not require a mortgage since you can put down more than the mortgage amount"
    if downPercentage < MIN_DOWN_PERCENTAGE:
        return "You do not qualify for a mortgage. You need a down payment of at least 5 percent of the house cost."
    if salaryPercentage < MIN_SALARY:
        return "You do not qualify for a mortgage. You need a salary of at least 10 percent of the house cost."
    return "Congratulations! You qualify for a mortgage."

def cape_handler(input_data):
    input_data = json.loads(input_data)
    salary = input_data["salary"]
    amount = input_data["amount"]
    down = input_data["down"]
    return mortgage(salary, amount, down)
