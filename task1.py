from qlib.payoff import Payoff
from qlib.misc import read_config
from qlib.BlackScholes import BSCalculator


if __name__ == "__main__":
    run_config = read_config(config_path="config.yml")

    analytical_calculator = BSCalculator(market_params=run_config.market_params, stock_params=run_config.stock_params)

    # European digital
    digital_call_payoff = Payoff.european_digital(option_type="call", params=run_config.option_params)
    digital_price = analytical_calculator.price(digital_call_payoff)  # 0.46397559
    digital_delta = analytical_calculator.delta(digital_call_payoff)  # 1.98212847

    print(digital_call_payoff)
    print(f"\nprice = {digital_price}")
    print(f"delta = {digital_delta}")

    # European option
    call_option_payoff = Payoff.european_option(option_type="call", params=run_config.option_params)
    option_price = analytical_calculator.price(call_option_payoff)  # 0.08081098
    option_delta = analytical_calculator.delta(call_option_payoff)  # 0.54478657

    print(f"\n\n{call_option_payoff}")
    print(f"\nprice = {option_price}")
    print(f"delta = {option_delta}")
