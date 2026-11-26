# Assignment 1: Multi-Gateway Payment Processing Engine

- **Author:** Pranjal Khadke
- **Email:** [Pranjalckhadke@gmail.com](mailto:Pranjalckhadke@gmail.com)
- **GitHub:** [@PranjalKhadke](https://github.com/PranjalKhadke)
- **Course:** AIML Honors &bull; Semester III

An object-oriented payment processing simulator built using the Factory Method pattern and Polymorphism in Python.

### Features
- **Gateways Supported:** Razorpay (2.0% fee), Stripe (2.9% fee), Paytm (1.8% fee).
- **Payment Methods:** Credit/Debit Card (with masking and length validation), UPI (with VPA validation), NetBanking.
- **Dynamic Fee Calculation:** Automatically computes subtotal, transaction charges, and grand total.

### Files
- `gateways.py`: Abstract base class `PaymentGateway` and concrete gateway classes with factory registry.
- `payment_methods.py`: Base class `PaymentMode` with concrete implementations (`CardPayment`, `UPIPayment`, `NetBankingPayment`).
- `main.py`: Interactive CLI interface and automated test runner.
- `assignment1.ipynb`: Executed Jupyter Notebook showing end-to-end demonstrations and receipts.

### How to Run
```bash
python main.py
```
Or open `assignment1.ipynb` in VS Code / Jupyter Lab to view the interactive runs.
