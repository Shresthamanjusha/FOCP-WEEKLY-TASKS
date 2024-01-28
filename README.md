# FOCP-WEEKLY-TASKS
#Task1
The code defines a pizza price calculator using a function calculate_price that considers factors such as the day of the week (Tuesday discounts), the number of pizzas, delivery option, and app usage to determine the total price. It then takes user input for the number of pizzas, whether it's Tuesday, delivery preference, and app usage to calculate and display the total price in pounds with appropriate discounts.

Output
BPP Pizza Price Calculator
==========================
How many pizzas would you like to order? -3
Please enter a positive integer!
How many pizzas would you like to order? 3
Is it Tuesday? a
Please answer "y" or "n".
Is it Tuesday? y
Is delivery required? n
Did the customer use the app? n

Total Price: £18.00
Task2
The code defines a function analyze_log to read and analyze a log file containing information about cat entries and water dousing incidents. It calculates various statistics such as the total number of correct cat entries, instances of cats being doused with water, total time spent by the correct cat, average visit duration, and extremes in visit durations. The script takes the log file path as a command-line argument and prints the analysis results.

The if __name__ == "__main__": block ensures that the script is executed when run as the main program, and it checks if the correct number of command-line arguments is provided before calling the analyze_log function and printing a separator line.
Output
(base) manjusha@Manjushas-MacBook-Air Task2 % Python catshelter.py shelter_2023-08-27.log
Log File Analysis
=================
Total number of times the correct cat has entered the house is: 13
Number of times cats were doused with water: 53
Total time spent in the house by the correct cat: 5.83 hours
Average duration of each visit by the correct cat: 26.92 minutes
Duration of the longest visit by the correct cat: 50 minutes
Duration of the shortest visit by the correct cat: 5 minutes
=======================


