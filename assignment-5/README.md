# Assignment 5: Function Decorators

- **Author:** Pranjal Khadke
- **Email:** [Pranjalckhadke@gmail.com](mailto:Pranjalckhadke@gmail.com)
- **GitHub:** [@PranjalKhadke](https://github.com/PranjalKhadke)
- **Course:** AIML Honors &bull; Semester III

Implementation of custom Python decorators showcasing parameter inspection, performance benchmarking, input validation, and decorator stacking using `functools.wraps`.

### Decorators Implemented
1. `@time_execution`: Benchmarks execution duration using `time.perf_counter()`.
2. `@log_calls(tag=...)`: Tracks function name, positional arguments, keyword arguments, and return values.
3. `@validate_positive`: Validates that numerical arguments are positive before function execution.
4. **Stacked Decorators**: Chains validation, logging, and timing on computational financial formulas.

### Files
- `decorators.py`: Decorator definitions, decorated functions, and test suite.
- `assignment5.ipynb`: Fully executed Jupyter notebook with outputs.

### How to Run
```bash
python decorators.py
```
Or open `assignment5.ipynb` in VS Code or Jupyter Lab.
