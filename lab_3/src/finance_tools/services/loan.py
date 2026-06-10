from ..core.validators import validate_amount, validate_rate, validate_year

class LoanCalculator:
    """Класс для расчёта аннуитетных платежей по кредиту"""
    
    def __init__(self, amount: float, rate: float, years: int):
        validate_amount(amount)
        validate_rate(rate)
        validate_year(years)
        
        self.amount = amount
        self.rate = rate
        self.years = years
    
    def _monthly_rate(self) -> float:
        """Месячная процентная ставка в долях"""
        return self.rate / 100 / 12
    
    def _months(self) -> int:
        """Срок кредита в месяцах"""
        return self.years * 12
    
    def annuity_payment(self) -> float:
        """
        Аннуитетный платеж (ежемесячный)
        Формула: П = С * (М / (1 - (1 + М)^-n))
        где С — сумма кредита, М — месячная ставка, n — кол-во месяцев
        """
        M = self._monthly_rate()
        n = self._months()
        
        if M == 0:
            return round(self.amount / n, 2)
        
        payment = self.amount * (M / (1 - (1 + M) ** -n))
        return round(payment, 2)
    
    def total_payment(self) -> float:
        """Общая сумма выплат за весь срок"""
        return round(self.annuity_payment() * self._months(), 2)
    
    def total_interest(self) -> float:
        """Сумма переплаты по процентам"""
        return round(self.total_payment() - self.amount, 2) 
