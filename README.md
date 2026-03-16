# Processor Design Task 2

## Overview
This project is a Boolean expression simplifier designed as part of a Computer Architecture / Processor Design course assignment. It allows users to:
  -Input a truth table (from a file or generate randomly)
  -Automatically generate the canonical Boolean expression (SOP or POS)
  -Display the Karnaugh Map (K-map) for 2–4 variables
  -Simplify the Boolean expression using K-map grouping
  -Validate the simplified expression against the original truth table

  ## Features
  Truth Table Input:
    -From a .txt file or automatically generated random truth table
  
  Supports 2–4 Variables:
    -Generates correct K-map layout for 2, 3, or 4 variables

  Canonical Expression Generation:
    -SOP (Sum of Products)
    -POS (Product of Sums)

  K-map Simplification:
    -Finds largest possible groups for simplification
    -Handles wrap-around groups automatically
  
  Validation:
    -Evaluates simplified expression for all input combinations
    -Compares against original truth table to ensure correctness

## File Structure
```
ProcessorDesignTask2/
│
├─ main.py                     # Main program file
├─ kmapFunctions.py            # Functions to build and display K-map
├─ groupingFunctions.py        # Functions to find and convert K-map groups to terms
├─ validationFunctions.py      # Functions to validate simplified expressions
├─ truthTable.txt              # Sample truth table file
└─ README.md                   # This file
```

## Usage
  python main.py

Truth Table as Input
  truthTable.txt:
    00001111

  This would represent a truth table with 3 variables and these are the outputs of that table.
  Ex:
  ```
    Truth Table
      A | B | C | Y
      -------------
      0 | 0 | 0 | 0
      0 | 0 | 1 | 0
      0 | 1 | 0 | 0
      0 | 1 | 1 | 0
      1 | 0 | 0 | 1
      1 | 0 | 1 | 1
      1 | 1 | 0 | 1
      1 | 1 | 1 | 1
  ```

Program Flow:
  1. Enter the number of variables (n ≥ 2).
  2. Enter the form: SOP or POS.
  3. Choose whether to use a random truth table or a file (truthTable.txt).
  4. The program will display:
    -Truth Table
    -Boolean Expression (canonical form)
    -Karnaugh Map
    -Simplified Boolean Expression
    -Validation result
