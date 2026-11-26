from abc import ABC
import random
from payment_methods import CardPayment, UPIPayment, NetBankingPayment


class PaymentGateway(ABC):
    def __init__(self, name, fee_rate, support_email):
        self.name = name
        self.fee_rate = fee_rate
        self.support_email = support_email

    def calculate_fee(self, amount):
        return round(amount * self.fee_rate, 2)

    def process_transaction(self, mode, amount):
        print("=" * 64)
        print(f"          {self.name.upper()} PAYMENT PROCESSING ENGINE")
        print("=" * 64)

        if amount <= 0:
            print(f"  [Rejection] Transaction declined: Amount (Rs. {amount}) must be > 0.")
            print("=" * 64 + "\n")
            return False

        txn_id = f"{self.name[:2].upper()}-TXN-{random.randint(100000, 999999)}"
        fee = self.calculate_fee(amount)
        final_bill = amount + fee

        print(f"  Transaction ID : {txn_id}")
        print(f"  Gateway Node   : {self.name} Central Switch")
        print(f"  Payment Mode   : {mode.get_summary()}")
        print("-" * 64)
        print(f"  Base Amount    : Rs. {amount:>12,.2f}")
        print(f"  Processing Fee : Rs. {fee:>12,.2f}  ({self.fee_rate * 100:.1f}%)")
        print(f"  Grand Total    : Rs. {final_bill:>12,.2f}")
        print("-" * 64)

        success = mode.process_charge(final_bill, txn_id)

        print("-" * 64)
        if success:
            print("  Transaction Status : SUCCESSFUL (HTTP 200 OK)")
        else:
            print("  Transaction Status : FAILED / REJECTED")
        print("=" * 64 + "\n")
        return success


class RazorpayGateway(PaymentGateway):
    def __init__(self):
        super().__init__("Razorpay", 0.02, "support@razorpay.com")


class StripeGateway(PaymentGateway):
    def __init__(self):
        super().__init__("Stripe", 0.029, "support@stripe.com")


class PaytmGateway(PaymentGateway):
    def __init__(self):
        super().__init__("Paytm", 0.018, "care@paytm.com")


GATEWAY_MAP = {
    "razorpay": RazorpayGateway,
    "stripe": StripeGateway,
    "paytm": PaytmGateway,
}


def get_gateway(gateway_name):
    key = gateway_name.strip().lower()
    if key not in GATEWAY_MAP:
        supported = ", ".join(GATEWAY_MAP.keys())
        raise ValueError(f"Gateway '{gateway_name}' not configured. Available options: {supported}")
    return GATEWAY_MAP[key]()
