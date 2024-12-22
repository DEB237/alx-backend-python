# Unit and Integration Testing in Python

## Overview
Unit testing ensures individual functions work as expected with various inputs. Integration testing verifies the interactions between multiple components.

---

## Unit Testing
- **Purpose**: Test function logic in isolation.
- **Characteristics**:
  - Test standard and edge inputs.
  - Mock external calls (e.g., HTTP, database queries).
- **Key Question**: Does the function work as expected when external dependencies behave correctly?
- **Run**: 
  ```bash
  $ python -m unittest path/to/test_file.py
  ```

---

## Integration Testing
- **Purpose**: Test interactions across components end-to-end.
- **Mocks**: Limit to low-level external calls like HTTP or database I/O.

---

## Key Resources
- **[unittest](https://docs.python.org/3/library/unittest.html)**: Python’s built-in testing framework.
- **[unittest.mock](https://docs.python.org/3/library/unittest.mock.html)**: Mocking library.
- **[parameterized](https://pypi.org/project/parameterized/)**: For parameterized tests.

---

## Project Requirements
1. Files must run on **Ubuntu 18.04 LTS** with Python 3.7.
2. Follow **pycodestyle** guidelines.
3. Include proper documentation for modules, classes, and functions.
4. Use type annotations in all functions.

---

## Files
- **`utils.py`**: Utility functions.
- **`client.py`**: Client-side logic.
- **`fixtures.py`**: Sample data and test fixtures.

