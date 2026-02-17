Student Attendance System

Description:
The Student Attendance System is a simple Python console application that manages daily student attendance using a set data structure. It ensures that no duplicate attendance entries are recorded.

Features:

1. Mark Attendance
   - Enter student name to mark as present.
   - Prevents duplicate entries automatically.

2. View Attendance
   - Displays all students marked present for the session.

3. Check Student
   - Checks whether a specific student is present or absent.

4. Remove Attendance
   - Removes a student's attendance record if needed.

5. Exit
   - Safely exits the program.

How It Works:
- Attendance data is stored in a Python set.
- A set is used because it does not allow duplicate values.
- The program runs in a loop and provides a menu-driven interface.
- The user selects options to perform different operations.

Technologies Used:
- Python
- Set Data Structure
- Functions
- Loops
- Conditional Statements

Advantages of Using Set:
- No duplicate attendance entries.
- Fast lookup and removal operations.
- Simple and efficient structure.

Limitations:
- Data is stored only in memory.
- Attendance records are lost after the program closes.
- No date-wise tracking.

Future Improvements:
- Add file handling to save attendance permanently.
- Add date tracking for daily attendance.
- Calculate attendance percentage.
- Convert into OOP-based structure.
- Create a GUI version using Tkinter.
- Convert into a web-based system using Flask or Django.

Author:
Aditya

Purpose:
This project is designed to help beginners understand Python sets, menu-driven programming, and basic system design concepts.
