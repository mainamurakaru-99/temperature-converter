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
Key activities include:

Branching: Each contributor works on separate branches to isolate changes and prevent conflicts in the main codebase.

Merging: Completed features are reviewed and merged into the main branch after verification, ensuring controlled integration.

Collaborative Review: Team members perform peer reviews through pull requests, adding comments and suggestions before merging.

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
