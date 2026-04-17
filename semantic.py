def run_semantic():
    print("\n--- PHASE 3: SEMANTIC ANALYSIS ---\n")
    print("Enter statements (type 'exit' to stop)\n")

    symbol_table = set()

    while True:
        line = input(">> ").strip()
        if line.lower() == "exit":
            break
        if not line:
            continue
        if line.endswith(";"):
            line = line[:-1]
        if line.startswith("int"):
            parts = line.split()

            if len(parts) >= 2:
                variables = parts[1].split(",")

                for var in variables:
                    var = var.strip()

                    if var in symbol_table:
                        print(f"ERROR: {var} already declared")
                    else:
                        symbol_table.add(var)
                        print(f"Declared: {var}")
            else:
                print("Invalid declaration")
        elif "=" in line:
            lhs, rhs = line.split("=", 1)
            lhs = lhs.strip()
            rhs = rhs.strip()

            if lhs not in symbol_table:
                print(f"ERROR: {lhs} not declared")
            else:
                print(f"OK: {line}")

        else:
            print("Invalid statement")

    print("\nFinal Symbol Table:", symbol_table)

if __name__ == "__main__":
    run_semantic()

