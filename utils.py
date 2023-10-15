from datetime import datetime
from dateutil.relativedelta import relativedelta

def add_years_to_date(original_date, years_to_add):
    result = original_date + relativedelta(years=+years_to_add)
    return result