# day 12 task
# name : khushi
# waht i learned :file handling, exception handling, data processing,dry run, functions & dictionaries
# where i got stuck: try except , split, enumerat

"""
Part A: Dry Run

1. audit_ledger([10, 20])
   Output: [10, 20, 40]
   Reason: 20 * 2 = 40

2. audit_ledger([])
   Output: Empty
   Reason: IndexError (empty list)

3. audit_ledger([5, "10"])
   Output: [5, '10', '1010']
   Reason: String repetition
"""

# Part A: Dry Run function
def audit_ledger(data, factor=2):
    try:
        data.append(data[-1] * factor)
    except IndexError:
        return "Empty"
    except Exception as e:
        return f"Err: {e}"
    else:
        return data

# Part B: Process employee records
def process_records(input_filepath, output_filepath):
    payouts = {}

    try:
        with open(input_filepath, "r") as file:
            for line_no, line in enumerate(file, 1):
                try:
                    parts = line.strip().split(",")

                    if len(parts) != 3:
                        raise ValueError("Invalid fields")

                    name = parts[0].strip()
                    hours = float(parts[1])
                    rate = float(parts[2])

                    if not name or hours < 0 or rate < 0:
                        raise ValueError("Invalid data")

                    payouts[name] = payouts.get(name, 0) + hours * rate

                except (ValueError, IndexError) as e:
                    print(f"Line {line_no}: {e}")

    except FileNotFoundError:
        print("Input file not found.")
        return

    try:
        with open(output_filepath, "w") as file:
            for name, payout in payouts.items():
                file.write(f"{name}: ₹{payout:.2f}\n")

        print("Summary generated.")

    except OSError as e:
        print(f"Output error: {e}")


# Main program
if __name__ == "__main__":
    process_records("audit_input.txt", "audit_summary.txt")