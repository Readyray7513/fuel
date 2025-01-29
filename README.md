# Fuel Status Validator

## Overview
This program prompts the user to input fuel status as a fraction in the format "X/Y". It performs various checks to ensure the input is valid. If the input is incorrect (such as a non-integer, division by zero, or invalid fraction), the program asks the user to try again. Based on the valid input, it calculates the fuel status as either full ('F'), empty ('E'), or a percentage of fuel remaining.

## Features
- The program ensures that both "X" and "Y" are integers.
- It handles special cases, such as when "Y" is zero or when "X" is greater than "Y".
- The program calculates the fuel percentage and prints the status:
  - 'F' for full (99% or more),
  - 'E' for empty (10% or less),
  - a percentage for values in between.
- It handles errors like `ValueError` (non-integer inputs) and `ZeroDivisionError` (when "Y" is zero).

## Example Usage
```
$ python fuel_status.py
Type fuel status in fraction, X/Y format: 3/4
75%
```

```
$ python fuel_status.py
Type fuel status in fraction, X/Y format: 5/4
X cannot be greater than Y. Please try again.
```

```
$ python fuel_status.py
Type fuel status in fraction, X/Y format: 4/0
Y cannot be zero. Please try again.
```

## How to Run
1. Run the program by executing:
   ```
   python fuel_status.py
   ```
2. Enter the fuel status in the "X/Y" format when prompted.
3. If the input is invalid, the program will prompt the user again until valid input is received.
4. Once valid input is entered, the program will display the fuel status (either 'F', 'E', or the percentage).

## Notes
- The program uses exception handling to manage incorrect inputs (non-integer fractions, zero in the denominator, etc.).
- The user can keep entering new values until a valid input is provided.
