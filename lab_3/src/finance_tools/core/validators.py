from ..exceptions import InvalidRateError, NegativeAmountError, InvalidYearError

def validate_rate(rate: float) -> None:
    """Проверяет, что процентная ставка в диапазоне 0..100"""
    if rate < 0 or rate > 100:
        raise InvalidRateError(f"Процентная ставка должна быть от 0 до 100, получено: {rate}")

def validate_amount(amount: float) -> None:
    """Проверяет, что сумма не отрицательная"""
    if amount < 0:
        raise NegativeAmountError(f"Сумма не может быть отрицательной: {amount}")

def validate_year(years: int) -> None:
    """Проверяет, что срок кредита положительный"""
    if years <= 0:
        raise InvalidYearError(f"Срок кредита должен быть больше 0, получено: {years}") 
