from antlr4 import *
from python_pd3Parser import python_pd3Parser
from python_pd3Lexer import python_pd3Lexer


def main():
    with open("project_deliverable_3.py", "r") as file:
        input_code = file.read()

    input_stream = InputStream(input_code)

    # Use CustomLexer instead of python_pd3Lexer
    lexer = python_pd3Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = python_pd3Parser(token_stream)

    # Parse the input
    tree = parser.program()
    print(tree.toStringTree(recog=parser))

    for _ in range(5):
        print()



if __name__ == "__main__":
    main()
