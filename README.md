# MathSprints
Generate math problem sets at different difficulty

This README will be hashed out further in the next 2 weeks - 1 month

This repository is for code that facilitates Primary and Secondary mathematics education.

The current projects under development are a backend library that can be used to generate 
worksheets that are designed to target specific math skills (basic arithmetic, times tables, fractional arithmetic, etc...)

The idea is that these fundamental math skills are cultivated mainly through 
repetitious practice to develop pattern recognition. These types of teaching materials are tedious to create and tedious
to assess/grade. Automating these processes through worksheet a worksheet and answer-sheet generator can allow instructors
to spend more time with other aspects of mathematical instruction as well as provide ample 
practice materials that are closely aligned with a wide range of abilities.

Currently, the repo contains:
* a backend problem generator that supports basic arithmetic problems for integers and fractions. 
* a desktop GUI written in PYQT5 that is in development. This GUI provides flexible worksheet-layout controls and supports 
worksheet publishing to PDFs

Areas for further development include:
* Extension of backed capabilities for more advanced problem types 
  (incorporation of parentheses, one-step algebra, mulit-step algebra, exponents, roots, logs and many others)
* Extension of the backend to output problems in MathML (https://www.w3.org/Math/)
* Extension of the backend to calculate the answers to the problems to facilitate answer-sheet generation
* An alternative web-hosted front end including user accounts, saved problem set configs, etc...
* Using a Handwriting-to-text ML model to implement photo-based auto-grader
* A database of Worksheet/problem set configs that are aligned to common-core standards and other educational standards.
