from get_net_order_value import get_net_order_value
from get_final_output import get_final_output

def app() -> None:
  net_order_value = get_net_order_value()
  get_final_output(net_order_value)

app()