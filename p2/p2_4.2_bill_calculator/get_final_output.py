from constants import VAT, ROUND_NUMBER, DEFAULT_TIPS, RUB_SYMBOL
from utils import get_added_value, get_formatted_number

def get_final_output(net_value: float) -> None:
  vat_amount: float = round(get_added_value(net_value, VAT), ROUND_NUMBER)
  tips_amount: float = round(get_added_value(net_value, DEFAULT_TIPS), ROUND_NUMBER)
  total_amount: float = round(net_value + vat_amount + tips_amount, ROUND_NUMBER)

  final_output = f'''
  +++
  Сумма заказа: {get_formatted_number(net_value)} {RUB_SYMBOL}
  Сумма НДС {VAT}%: {get_formatted_number(vat_amount)} {RUB_SYMBOL}
  Сумма чаевых {DEFAULT_TIPS}%: {get_formatted_number(tips_amount)} {RUB_SYMBOL}
  =====
  ИТОГО: {get_formatted_number(total_amount)} {RUB_SYMBOL}
  +++
  '''

  print(final_output)
