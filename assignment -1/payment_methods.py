from abc import ABC, abstractmethod
import time


class PaymentMode(ABC):
    @abstractmethod
    def get_summary(self):
        pass

    @abstractmethod
    def process_charge(self, total_amt, txn_id):
        pass


class CardPayment(PaymentMode):
    def __init__(self, card_number, holder_name=""):
        clean_num = str(card_number).replace(" ", "").replace("-", "")
        self.card_number = clean_num
        self.holder_name = holder_name.strip()

    def get_summary(self):
        masked = f"****-****-****-{self.card_number[-4:]}" if len(self.card_number) >= 4 else self.card_number
        holder = f" [{self.holder_name}]" if self.holder_name else ""
        return f"Debit/Credit Card {masked}{holder}"

    def process_charge(self, total_amt, txn_id):
        if len(self.card_number) != 16 or not self.card_number.isdigit():
            print("  [Validation Error] Card number must contain exactly 16 numeric digits.")
            return False
        print(f"  [Card Network] Authorizing Rs. {total_amt:,.2f} on card {self.card_number[-4:]}...")
        print(f"  [Card Network] Payment authorized successfully under {txn_id}.")
        return True


class UPIPayment(PaymentMode):
    def __init__(self, vpa):
        self.vpa = vpa.strip()

    def get_summary(self):
        return f"Unified Payments Interface (UPI) [VPA: {self.vpa}]"

    def process_charge(self, total_amt, txn_id):
        if "@" not in self.vpa or self.vpa.startswith("@") or self.vpa.endswith("@"):
            print("  [Validation Error] Invalid UPI Virtual Payment Address format (expected user@psp).")
            return False
        print(f"  [UPI Gateway] Dispatching collect request of Rs. {total_amt:,.2f} to {self.vpa}...")
        print(f"  [UPI Gateway] PIN verified on device. Response code: 00 (Success).")
        return True


class NetBankingPayment(PaymentMode):
    def __init__(self, bank_name, user_id=""):
        self.bank_name = bank_name.strip()
        self.user_id = user_id.strip()

    def get_summary(self):
        uid = f" (User: {self.user_id})" if self.user_id else ""
        return f"Internet Banking [{self.bank_name}{uid}]"

    def process_charge(self, total_amt, txn_id):
        if not self.bank_name:
            print("  [Validation Error] Bank name cannot be empty for NetBanking.")
            return False
        print(f"  [Bank Gateway] Secure handshake with {self.bank_name} Core Banking Server...")
        print(f"  [Bank Gateway] 2FA OTP validated. Debited Rs. {total_amt:,.2f}.")
        return True
