# Project Statement

## Project Title

Integration Solver

---

## 1. Problem Statement

Polynomial integration is a fundamental mathematical operation, but manually integrating polynomial expressions can become repetitive and prone to calculation or sign errors, especially when an expression contains multiple terms, negative coefficients, constants, and different powers of x.

The objective of this project is to develop a Python-based Integration Solver that accepts a polynomial expression as input, validates the expression, separates individual terms into their coefficients and powers, applies the polynomial power rule of integration, and generates the resulting integrated expression.

The project demonstrates the practical application of Python programming concepts such as functions, modules, lists, string processing, conditional statements, loops, input validation, and automated testing.

---

## 2. Scope of the Project

The current version of the Integration Solver is focused on indefinite integration of basic polynomial expressions in one variable, x.

The system includes:

- Validation of polynomial input
- Separation of polynomial terms
- Extraction of coefficients and powers
- Integration using the polynomial power rule
- Construction of a readable output expression
- Automated testing of major components

The current scope does not include:

- Trigonometric integration
- Logarithmic integration
- Exponential integration
- Integration by parts
- Substitution
- Definite integration
- Multiple-variable integration
- Advanced symbolic mathematical operations

---

## 3. Target Users

The project is primarily intended for:

- Students learning polynomial integration
- Beginners learning Python programming
- Users who need to quickly integrate basic polynomial expressions
- Students interested in understanding how mathematical operations can be implemented programmatically

---

## 4. High-Level Features

### 4.1 Input Validation

The system checks whether the entered expression follows the supported polynomial format before processing it.

### 4.2 Polynomial Term Extraction

The expression is separated into individual terms, and each term is represented using its coefficient and power.

For example:

```text
3x^2 + 4x - 7