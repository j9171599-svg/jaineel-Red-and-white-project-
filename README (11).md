# Student Data Organizer

A simple command-line application written in Python to manage student records. Created by **Jaineel Shingala**.

## Features

- **Add Student**: store ID, name, age, grade, date of birth and subjects
- **Display All Students**: view every saved student record
- **Update Student Information**: edit the details of an existing student
- **Delete Student**: remove a student by ID
- **Display Subjects Offered**: list the subjects available (Math, Science, English)
- **Exit**: close the program

## Requirements

- Python 3.x (no external libraries needed)

## How to Run

1. Save the code as `student_organizer.py` (or keep your existing file name).
2. Open a terminal or Python IDLE.
3. Run:

```bash
python student_organizer.py
```

## Menu Options

```
Select an option:
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
```

Enter the number of the option you want and follow the prompts.

## Screenshots

### Adding Students

![Adding students](screenshot1.png)

### Updating and Displaying Students

![Updating and displaying students](screenshot2.png)

## How It Works

- Student records are stored in a Python dictionary, with the Student ID as the key.
- Each record holds: `name`, `age`, `grade`, `dob` and `subjects`.
- Adding a student with an ID that already exists is rejected.
- Updating or deleting an ID that doesn't exist shows a "not found" message.
- Data is kept in memory only, so records are lost when the program exits.

## Known Limitations / Future Improvements

- No input validation (for example, age `198` or a date of birth like `222222` are accepted).
- Updating a student overwrites every field, so leaving a prompt blank erases that value (as seen in the second screenshot).
- Deleting a student ID that doesn't exist prints no message.
- Records are not saved to a file or database.
- Subjects are entered as free text instead of being chosen from the subjects offered.

## Author

Jaineel Shingala
