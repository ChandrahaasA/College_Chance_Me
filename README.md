# College Chance Me
My first Python project. You type in your unweighted GPA and ACT score, pick some Minnesota colleges, and it tells you if each one is a Reach, Match, or Likely.

## How it works
It compares your numbers to the middle 50% ranges of students each college admitted. Below the range is a Reach, inside is a Match, and above is Likely. If a college gives both an ACT and a GPA range, it uses whichever one is lower.

## Run it
python app.py

## Where the numbers came from
- UMN Twin Cities admissions page (Fall 2025 admitted students)
- St. Thomas Quick Facts page
- Carleton Common Data Set
- Minnesota State Mankato profile on CollegeData

## Things to know
- This isn't a real prediction. Colleges also look at classes, activities, and other stuff.
- Some of these colleges are test optional, so the ranges only cover students who sent scores.

## Notes
I'm still learning Python. I used Claude and youtube tutorials to help, mostly for the bug fixing and getting the admissions data, and wrote the rest myself. Next I want to add more colleges and use the SAT too. And work on other websites, like a game or something.
