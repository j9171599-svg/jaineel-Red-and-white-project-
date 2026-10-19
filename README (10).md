# Pattern Generator and Number Analyzer

A simple menu-driven Python program that generates a star pattern and analyzes a range of numbers.

**Author:** Jaineel Shingala
**Guided by:** Girish Sir

---

## Features

1. **Generate a Pattern** – Prints a star (`*`) pattern for the number of rows you enter.
2. **Analyze a Range of Numbers** – Takes a start and end number, shows whether each number is Even or Odd, and prints the sum of all numbers in the range.
3. **Exit** – Closes the program.

The menu keeps repeating until you choose Exit. An invalid choice shows an error message and returns to the menu.

## Requirements

- Python 3.x

## How to Run

1. Save the program file (`jaineel python project2 - Copy.py`).
2. Open a terminal or Python IDLE.
3. Run:

   ```
   python "jaineel python project2 - Copy.py"
   ```

## Example Output

Output from running the program in Python IDLE:

```
Welcome to the Pattern Generator and Number Analyzer!

Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit
Enter your choice: 2
Enter the start of the range: 1
Enter the end of the range: 10
Number 1 is Odd
Number 2 is Even
Number 3 is Odd
Number 4 is Even
Number 5 is Odd
Number 6 is Even
Number 7 is Odd
Number 8 is Even
Number 9 is Odd
Number 10 is Even
Sum of all numbers from 1 to 10 is: 55

Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit
Enter your choice: 1
Enter the number of rows for the pattern: 5
**
***
****
*****
******

Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit
```

<!-- Optional: to show the actual screenshot, save it as screenshot.png in this folder and uncomment the line below -->
<!-- ![Program Screenshot](screenshot.png) -->


## Concepts Used

- `while` loop for the repeating menu
- `for` loop with `range()`
- `if / elif / else` conditions
- Modulus operator (`%`) for even/odd checking
- f-strings for formatted output
- User input with `input()` and `int()`

## Author

Jaineel Shingala

Guided by Girish Sir
