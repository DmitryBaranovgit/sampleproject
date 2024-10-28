from calculator.basic_operations import add, subtract
from calculator.advanced_operations import power

class Calculator:
    """Калькулятор, выполняющий базовые и сложные операции."""

    def calculate(self, operation, a, b):
        """Выполняет операцию с двумя числами.

        Args:
            operation (str): Тип операции ('add', 'subtract', 'power').
            a (float): Первое число.
            b (float): Второе число.

        Returns:
            float: Результат операции.

        Raises:
            ValueError: Если передана неподдерживаемая операция.
        """
        if operation == 'add':
            return add(a, b)
        elif operation == 'subtract':
            return subtract(a, b)
        elif operation == 'power':
            return power(a, b)
        else:
            raise ValueError("Unsupported operation")
