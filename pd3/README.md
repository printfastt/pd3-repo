Python Project Deliverable 3 Parser  //CS4450
Project Description
This project implements a parser for a Python-like grammar using ANTLR4. The parser processes Python code from a file named project_deliverable_3.py, tokenizes it using a custom lexer, and parses the token stream into an abstract syntax tree (AST) using the provided grammar. The AST structure is printed as a tree to represent the program's syntax.

The parser supports Python constructs such as:

Variable assignments
Conditional statements (if, elif, else)
Loops (while, for)
Expressions and comparisons

Group Members:
Carson


Requirements:
Environment
Python 3.8 or higher
ANTLR 4.13.2 or compatible version
Required Libraries
Install the following Python libraries:

antlr4-python3-runtime: Use the specific version that matches your ANTLR version. For ANTLR 4.13.2:
bash: pip install antlr4-python3-runtime==4.13.2


Setup Steps:
Install ANTLR4: Download ANTLR4 and set it up for command-line usage. Instructions are available here: https://www.antlr.org/

Generate Lexer and Parser Code: Run the following command in the terminal to generate the lexer and parser:
bash antlr4 -Dlanguage=Python3 python_pd3.g4

This generates python_pd3Lexer.py and python_pd3Parser.py files.


Place Grammar Files: Ensure the python_pd3.g4 grammar file is in the same directory as the Python script.


How to Use/Run:
Running the Parser
Prepare Input Code: Save your Python-like code to a file named project_deliverable_3.py in the same directory as the parser.

Run the Script: Execute the script using Python:

bash python main.py
The script will:

Read the content of project_deliverable_3.py.
Tokenize and parse the content.
Print the abstract syntax tree to the console.
Example Usage
Input (project_deliverable_3.py): 

x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

(program (statement (assignment x = (expression 10))) (statement (if_block if (condition (expression x) > (expression 5)) : (block INDENT (statement print (expression "x is greater than 5")) DEDENT))))


Notes
The lexer and parser files are generated from the python_pd3.g4 grammar using ANTLR4.
The script includes a custom lexer to handle Python-style indentation tokens (INDENT, DEDENT).
For any issues, ensure your environment matches the requirements, and the grammar file is correctly defined.