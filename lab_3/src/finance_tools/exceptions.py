class FinanceError(Exception):
    """Базовое исключение для библиотеки finance_tools"""
    pass

class InvalidRateError(FinanceError):
    """Некорректная процентная ставка (отрицательная или > 100%)"""
    pass

class NegativeAmountError(FinanceError):
    """Отрицательная сумма денег"""
    pass

class InvalidYearError(FinanceError):
    """Некорректный срок кредита (0 или отрицательный)"""
    pass 
