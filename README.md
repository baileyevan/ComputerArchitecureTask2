Processor Design Task 2 – Karnaugh Map Simplifier

This project implements a Karnaugh Map (K-map) simplifier for Boolean expressions. It allows you to:

Load a truth table from a file.

Display the truth table.

Generate SOP (Sum of Products) or POS (Product of Sums) expressions.

Build and display the K-map.

Find groups in the K-map and simplify the Boolean expression.

Validate the simplified expression against the original truth table.

File Structure
ProcessorDesignTask2/
├─ main.py                  # Main program to run the K-map simplifier
├─ kmapFunctions.py         # Functions to build and print the K-map
├─ groupingFunctions.py     # Functions to find groups and convert them to Boolean terms
├─ validationFunctions.py   # Functions to validate simplified expressions against the truth table
├─ truthTable.txt           # Sample truth table input file
└─ README.md                # Project documentation
How to Use

Make sure Python 3 is installed.

Place your truth table in truthTable.txt (only 0 and 1, no spaces required).

Run the main program:

python main.py

Enter the number of variables (n >= 2) and choose SOP or POS.

The program will display:

The truth table.

The Boolean expression.

The Karnaugh Map.

The simplified expression.

Validation results.

Features

Supports 2–4 variable Boolean functions.

Handles both SOP and POS forms.

Groups K-map cells automatically and simplifies expressions.

Validates the simplified expression by evaluating all possible input combinations.

Generates random truth tables for testing (optional).
