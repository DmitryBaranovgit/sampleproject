class Logger:
    """Класс для логирования сообщений и результатов операций."""

    def log(self, message, result):
        """Выводит сообщение с результатом операции.

        Args:
            message (str): Описание операции.
            result (float): Результат операции.
        """
        print(f"{message} {result}")
