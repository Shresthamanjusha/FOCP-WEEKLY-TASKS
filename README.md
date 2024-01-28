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
Task3
1)adduser.py
The code defines a function add_user that takes new user information (username, real name, and password) and appends it to the 'passwd.txt' file in the format "username:real_name:password". In the main block, it obtains user input for a new user, checks if the chosen username already exists by reading existing usernames from the 'passwd.txt' file, and either prints an error message if the username is already in use or adds the new user to the file using the add_user function.

The code ensures the uniqueness of usernames before adding a new user to the 'passwd.txt' file, and it provides feedback to the user regarding the success or failure of the user creation process.

Output:
Enter new username: mk
Enter real name: manjusha
Enter password: meme
User Created.

2)login.py
The code defines a login function that checks the provided username and password against entries in the 'passwd.txt' file. It reads each line of the file, splits it into fields using ':' as a delimiter, and compares the username and password. If a match is found, it returns True indicating a successful login; otherwise, it returns False.

In the main block, the script takes user input for login credentials, calls the login function, and prints "Access granted." if the login is successful, or "Access denied." if the login fails. The code provides a basic authentication mechanism by validating user credentials against stored information in the 'passwd.txt' file.
Output:
User:     mshrestha
Password: hkhj
Access denied.





 


