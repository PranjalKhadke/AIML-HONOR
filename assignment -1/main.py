from gateways import get_gateway, GATEWAY_MAP
from payment_methods import CardPayment, UPIPayment, NetBankingPayment


def run_interactive():
    print("================================================================")
    print("               CAMPUS MULTI-GATEWAY PAYMENT ENGINE              ")
    print("================================================================")
    print("Configured Gateways:", " | ".join(GATEWAY_MAP.keys()))
    gw_choice = input("Enter Gateway: ").strip().lower()

    try:
        gateway = get_gateway(gw_choice)
    except ValueError as err:
        print(f"Error: {err}")
        return

    print("\nSelect Payment Method:")
    print("  1. Debit / Credit Card")
    print("  2. UPI (VPA)")
    print("  3. Internet Banking")
    method_choice = input("Choice (1/2/3): ").strip()

    if method_choice in ("1", "card"):
        card_num = input("Enter 16-digit Card Number : ").strip()
        holder = input("Enter Cardholder Name      : ").strip()
        mode = CardPayment(card_num, holder)
    elif method_choice in ("2", "upi"):
        vpa = input("Enter UPI Address (user@bank): ").strip()
        mode = UPIPayment(vpa)
    elif method_choice in ("3", "netbanking"):
        bank = input("Enter Bank Name (e.g. HDFC/SBI): ").strip()
        uid = input("Customer NetBanking ID         : ").strip()
        mode = NetBankingPayment(bank, uid)
    else:
        print("Invalid payment option selected.")
        return

    try:
        amt = float(input("Enter Transaction Amount (INR): "))
    except ValueError:
        print("Invalid amount entered. Transaction aborted.")
        return

    print("\nRouting request through gateway switch...\n")
    gateway.process_transaction(mode, amt)


def run_demo():
    print("================================================================")
    print("         AUTOMATED VERIFICATION SUITE - ASSIGNMENT 1            ")
    print("================================================================\n")

    # Case 1: Razorpay with UPI
    rp = get_gateway("razorpay")
    upi_mode = UPIPayment("pranjal.khadke@oksbi")
    rp.process_transaction(upi_mode, 1850.0)

    # Case 2: Stripe with Credit Card
    stripe_gw = get_gateway("stripe")
    card_mode = CardPayment("4532789012345678", "Pranjal Khadke")
    stripe_gw.process_transaction(card_mode, 4750.0)

    # Case 3: Paytm with NetBanking
    paytm_gw = get_gateway("paytm")
    nb_mode = NetBankingPayment("HDFC Bank", "CUST_7891")
    paytm_gw.process_transaction(nb_mode, 920.0)

    # Case 4: Validation guard test (Invalid Card Number)
    bad_card = CardPayment("1234", "Invalid Test")
    rp.process_transaction(bad_card, 500.0)

    # Case 5: Validation guard test (Negative Amount)
    rp.process_transaction(card_mode, -250.0)


if __name__ == "__main__":
    print("Select Execution Mode:")
    print("  1. Interactive Command Line")
    print("  2. Automated Test Suite (Default)")
    sel = input("Choice (1/2) [Enter for 2]: ").strip()
    if sel == "1":
        run_interactive()
    else:
        run_demo()
