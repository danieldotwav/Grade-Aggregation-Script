This Python script prompts the user to enter scores for four exams, sorts these scores, outputs the highest and lowest scores, provides a sorted list of these exam scores, calculates the average score excluding the lowest exam score, and finally assigns a letter grade based on this average.

## Features

- **Input Exam Scores:** Users can input scores for four separate exams.
- **Sorting Scores:** The program automatically sorts these scores in ascending order.
- **Highest and Lowest Scores:** Outputs both the highest and lowest exam scores.
- **Sorted List of Scores:** Displays the exam scores sorted from lowest to highest.
- **Average Score Calculation:** Calculates the average score based on the highest three exams.
- **Letter Grade Assignment:** Assigns a letter grade (A, B, C, D, or F) based on the average score.

## Usage

To use this script, you'll need a Python environment set up on your machine. Follow these steps:

1. **Start the Script:** Run the script in your Python environment.
2. **Enter Exam Scores:** When prompted, enter the scores for each of the four exams. Input should be a number that can be a floating point value for more precision.
3. **View Results:** After entering the scores, the script will automatically display:
   - The highest score.
   - The lowest score.
   - A sorted list of the scores from lowest to highest.
   - The average score based on the three highest exams.
   - The letter grade assigned based on the average score.

## Example
Please enter Exam 1 score: 85
Please enter Exam 2 score: 92
Please enter Exam 3 score: 78
Please enter Exam 4 score: 88

Highest score: 92.0
Lowest score: 78.0
Exams Entered: [78.0, 85.0, 88.0, 92.0]
Average Score (lowest exam dropped): 88.33
Grade: B - That's Great!

## Notes

- The program calculates the average score by excluding the lowest of the four exam scores to potentially enhance the overall grade.
- The grading scale used is as follows: A (90-100), B (80-89), C (70-79), D (60-69), and F (below 60).

## Contribution

Feel free to fork this repository to make changes or improvements. Pull requests are welcomed!