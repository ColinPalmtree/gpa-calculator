# GPA Calculator

COP 1500 Python group project - Colin Pearson & Sophia Ariza (Fall 2026)

Console program that keeps track of your classes by semester and calculates your semester GPA and cumulative GPA using FGCU's grading scale. It also has a "what if" calculator that shows what your GPA would be after classes you haven't taken yet.

## Running it

Needs Python 3, no extra libraries.

```
python main.py
```

There's example data in `sample_data/sample_student.txt` (option 9 to load it).

## What it can do

- add semesters and courses (grade can be a letter like B+ or a percent like 88)
- edit grades, remove courses / semesters
- transcript with semester GPA, cumulative GPA, credits earned and academic standing
- what if calculator
- save and load to a text file
- doesn't crash on bad input, it just asks again

GPA = total quality points / total credits, where quality points = grade points x credits.

## Files

- `main.py` - menu, input and printing
- `models.py` - Course, Semester, Student classes
- `grades.py` - FGCU grading scale and conversions
- `storage.py` - saving and loading
- `errors.py` - custom exceptions

## Sources

- Florida Gulf Coast University Academic Catalog, "Grade Point Average Calculation" (grade point values for each letter grade) - https://catalog.fgcu.edu/general-information/records-registration/grade-point-average-calculation/
- Python docs - https://docs.python.org/3/tutorial/
- OpenEDG Python Essentials 1 (Edube)
- COP 1500 class slides
