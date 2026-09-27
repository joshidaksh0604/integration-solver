# Integration Solver

A Python-based polynomial integration solver that parses mathematical expressions, validates user input, integrates polynomial terms using the power rule, and constructs the final result.

## Overview

The Integration Solver is a modular Python project designed to perform basic indefinite integration of polynomial expressions in terms of `x`.

The project takes a polynomial expression as input, validates the expression, separates its coefficients and powers, applies the power rule of integration, and displays the integrated expression.

## Features

- Accepts polynomial expressions in terms of `x`
- Validates user input
- Separates coefficients and powers from individual terms
- Integrates polynomial terms using the power rule
- Handles positive and negative coefficients
- Handles constants and terms with coefficient `1` or `-1`
- Constructs a readable final expression
- Includes automated tests using Python's `unittest` module
- Uses separate Python modules for different functionalities

## Project Structure

```text
integration-solver/
│
├── integration_solver.py
├── validator.py
├── coeff_pow_extract.py
├── polynomial.py
├── output_construct.py
├── test_solver.py
├── README.md
└── .gitignore