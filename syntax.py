import re

def syntax_analyzer(statement):

    statement = statement.strip()

    pattern = r'^[a-zA-Z_]\w*\s*=\s*([a-zA-Z_]\w*|\d+)(\s*[+\-*/]\s*([a-zA-Z_]\w*|\d+))?$'

    if re.match(pattern, statement):
        print(f"VALID SYNTAX   : {statement}")
    else:
        print(f"INVALID SYNTAX : {statement}")


print("SYNTAX ANALYSIS RESULT:\n")
print("Type 'exit' to stop.\n")

while True:
    statement = input("Enter a statement: ")

    if statement.lower() == "exit":
        print("Program terminated.")
        break

    if statement.strip():  # ignore empty input
        syntax_analyzer(statement)

