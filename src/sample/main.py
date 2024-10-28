from calculator.basic_operations import add, subtract
from calculator.advanced_operations import power
from utilities.logger import Logger
from models.calculator_model import Calculator

def main():
    """Главная функция, выполняющая основные операции калькулятора и логирование результатов."""
    logger = Logger()
    calculator = Calculator()

    result_add = add(10, 5)
    logger.log("Addition result:", result_add)

    result_subtract = subtract(10, 5)
    logger.log("Subtraction result:", result_subtract)

    result_power = power(2, 3)
    logger.log("Power result:", result_power)

    # Использование объекта калькулятора
    calc_result = calculator.calculate('add', 7, 3)
    logger.log("Calculator model result:", calc_result)

if __name__ == "__main__":
    main()
