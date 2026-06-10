from ..core.validators import validate_amount, validate_rate

def add_vat(amount: float, rate: float = 20) -> float:
    """Добавляет НДС к сумме"""
    validate_amount(amount)
    validate_rate(rate)
    return round(amount * (1 + rate / 100), 2)

def extract_vat(amount: float, rate: float = 20) -> float:
    """Выделяет НДС из суммы (сумма уже с НДС)"""
    validate_amount(amount)
    validate_rate(rate)
    vat = amount * rate / (100 + rate)
    return round(vat, 2)

def calculate_margin(cost: float, revenue: float) -> float:
    """Маржа = (выручка - себестоимость) / выручка * 100%"""
    validate_amount(cost)
    validate_amount(revenue)
    if revenue == 0:
        return 0.0
    margin = ((revenue - cost) / revenue) * 100
    return round(margin, 2)

def calculate_markup(cost: float, revenue: float) -> float:
    """Наценка = (выручка - себестоимость) / себестоимость * 100%"""
    validate_amount(cost)
    validate_amount(revenue)
    if cost == 0:
        return 0.0
    markup = ((revenue - cost) / cost) * 100
    return round(markup, 2)