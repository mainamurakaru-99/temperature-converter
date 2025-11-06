# Temperature Converter

A simple Python program for converting temperatures between Celsius and Fahrenheit.  
Created for **APT 2080 Lab** to demonstrate GitHub collaboration, branching, and peer review.  

**Contributors:**  
- Maina Murakaru (Maintainer)  - 672763
- Adan Badriyah (Collaborator)  - 672045
- Mohammed Dahir (Collaborator) - 673082
- Nyang'ara Nyamwange (Collaborator) - 670593

---

## Features
- Temperature Conversion (Celsius ↔ Fahrenheit)

The program enables accurate bidirectional conversion between Celsius and Fahrenheit temperature scales using standard mathematical formulas:

Celsius to Fahrenheit: (°C × 9/5) + 32

Fahrenheit to Celsius: (°F − 32) × 5/9

This feature illustrates the implementation of core programming logic and demonstrates how simple mathematical computations can be translated into a functional Python program. It provides instant, reliable results suitable for both academic and real-world use cases.

- Input Validation and Error Handling

The application integrates a simple input validation to ensure that only numeric temperature values are accepted.

If the user enters invalid input (e.g., text instead of a number), the program triggers a ValueError exception, prompting the user with a clear and friendly error message.

It also uses type checking to confirm that inputs are either integers or floating-point numbers.

This demonstrates the importance of defensive programming — preventing system crashes, improving user experience, and maintaining program reliability.
- Version Control and Collaboration (Git & GitHub)

The project follows structured version control practices using Git and GitHub to simulate a collaborative software development workflow.

Each team member contributed code updates or documentation through the shared repository.

GitHub was used to track project progress, store commits, and maintain a clear history of contributions.

The platform also supported collaborative review and easy access to the most updated version of the codebase.

---

Development model:

For this project, our team used the agile model of software development, which emphasizes flexibility and collaboration. We chose this because:

We handled separate parts of the project
We wanted to review each other’s work
We needed to go back and forth with the code
We worked collaboratively on GitHub

In summary, we chose agile because it allowed us to work simultaneously on different parts and change anything that was previously done.

Testing:
For this project we used 3 types of testing:
Unit Testing
Input Validation testing
Manual User testing

Unit testing
 
Unit tests were done to ensure the conversion formulas were correct. We did this by running the program with known values, from celsius to fahrenheit and fahrenheit to celsius, and confirming that the output results were all accurate. 

Input validation testing

These tests were to confirm how the program handles invalid input. We did this by putting in values that were not numbers, like text and characters, to confirm that the program would put out the correct error messages.

Manual User testing

This was to ensure the program was clear, understandable and easy to use. We did this by:
Making sure the input prompt is clear
Ensuring the output is formatted correctly and had the correct units
Ensuring execution was smoothly completed

Testing Outcome:

The testing process confirmed that The conversions were accurate, proper error messages were displayed when tests were done with invalid inputs, and the program is simple and easy to use.

---

## Collaboration and Testing
- Documentation, branching, merging and collaboration: Done by Maina Murakaru
- Module writing and unit testing: Done by Adan Badriyah
- Input-validation & exception-handling: Done by Mohammed Dahir
- All reviewed and approved each other's work through GitHub Pull Requests

---

## Usage
Run the module directly:
```bash
python temperature_converter.py
