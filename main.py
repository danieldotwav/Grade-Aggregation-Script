# Prompt the user for 4 exam scores
score1 = float(input("Please enter Exam 1 score: "))
score2 = float(input("Please enter Exam 2 score: "))
score3 = float(input("Please enter Exam 3 score: "))
score4 = float(input("Please enter Exam 4 score: "))

# Generate a list of scores and call the sort method
scores_list = [score1, score2, score3, score4]
scores_list.sort() # Now scores are in ascending order

# The first index of the list should have lowest exam score, the last index will have the highest exam score
# Output the highest score (index -1 or 3)
print(f"\nHighest score: {scores_list[-1]}")

# Output the lowest score (index 0)
print(f"Lowest score: {scores_list[0]}")

# Output the sorted exam score list from lowest to highest
print(f"Exams Entered: {scores_list}")

# Calculate and print the average score based on the 3 highest exams (indexes 1-3)
average_score = (sum(scores_list) - scores_list[0]) / (len(scores_list) - 1) # We need to exclude the lowest score from list and therefore its size it len - 1
print(f"Average Score (lowest exam dropped): {average_score:.2f}")

# Use an if statement to determine letter grade and print the appropriate message to user
message = ''
if average_score >= 90:
    message = "A - Good Job!"
elif average_score >= 80:
    message = "B - That's Great!"
elif average_score >= 70:
    message = "C - OK"
elif average_score >= 60:
    message = "D - Sorry"
else:
    message = "F - Try harder"

# Print letter grade and message
print(f"Grade: {message}")