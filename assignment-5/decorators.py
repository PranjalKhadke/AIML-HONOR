import time
from functools import wraps


def time_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  [PROFILER] {func.__name__}() elapsed time: {elapsed * 1000:.4f} ms ({elapsed:.7f} sec)")
        return result
    return wrapper


def log_calls(tag=None):
    def decorator(func):
        label = tag if tag else func.__name__.upper()

        @wraps(func)
        def wrapper(*args, **kwargs):
            arg_list = [repr(a) for a in args]
            kwarg_list = [f"{k}={repr(v)}" for k, v in kwargs.items()]
            call_repr = ", ".join(arg_list + kwarg_list)

            print(f"  [{label}] Calling {func.__name__}({call_repr})")
            result = func(*args, **kwargs)
            print(f"  [{label}] Returned -> {result}")
            return result
        return wrapper
    return decorator


def validate_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for idx, arg in enumerate(args):
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError(f"Positional argument at index {idx} ({arg}) must be strictly positive (> 0).")
        return func(*args, **kwargs)
    return wrapper


@log_calls(tag="ALGEBRA")
def compute_power(base, exponent):
    return base ** exponent


@time_execution
def sum_of_squares(n):
    return sum(i * i for i in range(1, n + 1))


@validate_positive
@log_calls(tag="FINANCE-ENGINE")
@time_execution
def calculate_compound_interest(principal, rate_pct, years):
    amount = principal * ((1 + rate_pct / 100) ** years)
    interest = round(amount - principal, 2)
    return interest


def run_demo():
    print("=" * 64)
    print("        PYTHON ADVANCED DECORATOR VERIFICATION SUITE           ")
    print("=" * 64 + "\n")

    print("[TEST 1] Testing Parameter & Output Introspection (@log_calls):")
    p = compute_power(2, 10)
    print(f"Final Computed Value: {p}\n")

    print("[TEST 2] Testing High-Precision Benchmarking (@time_execution):")
    total = sum_of_squares(100000)
    print(f"Sum of First 100,000 Squares: {total:,}\n")

    print("[TEST 3] Testing Stacked Decorators (@validate + @log + @time):")
    interest = calculate_compound_interest(50000, 7.5, 3)
    print(f"Accrued Compound Interest: Rs. {interest:,.2f}\n")

    print("[TEST 4] Testing Security Guard Rail Interception:")
    try:
        calculate_compound_interest(-25000, 6.0, 2)
    except ValueError as err:
        print(f"  [EXCEPTION INTERCEPTED] Validation Guard Triggered: {err}")
    print("\n" + "=" * 64)


if __name__ == "__main__":
    run_demo()
