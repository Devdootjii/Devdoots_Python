
# Day 12: Python Core + Integration Revision
# Name: Aryan
# What I learned: File Handling, Exception Handling,
# Data Processing, Dry Run, Functions and Dictionaries



#  Dry Run

def audit_ledger(data, factor=2):
    try:
        data.append(data[-1] * factor)
    except IndexError:
        return "Empty"
    except Exception as e:
        return f"Error: {e}"
    else:
        return data


print("===== PART A: DRY RUN =====")

print("\nScenario 1:")
print(f"Output: {audit_ledger([10, 20])}")

print("\nScenario 2:")
print(f"Output: {audit_ledger([])}")

print("\nScenario 3:")
print(f"Output: {audit_ledger([5, '10'])}")


#  Process Employee Records

def process_records(input_filepath, output_filepath):
    payouts = {}

    try:
        with open(input_filepath, "r") as input_file:

            for line_no, line in enumerate(input_file, start=1):
                try:
                    parts = line.strip().split(",")

                    if len(parts) != 3:
                        raise ValueError("Expected Name, HoursWorked, HourlyRate")

                    name = parts[0].strip()
                    hours = float(parts[1].strip())
                    rate = float(parts[2].strip())

                    if not name:
                        raise ValueError("Employee name is missing")

                    if hours < 0 or rate < 0:
                        raise ValueError("Hours and rate cannot be negative")

                    payout = hours * rate

                    payouts[name] = payouts.get(name, 0) + payout

                except ValueError as e:
                    print(f"Invalid record at line {line_no}: {e}")
                    continue

    except FileNotFoundError:
        print(f"Error: Input file '{input_filepath}' was not found.")
        return

    except OSError as e:
        print(f"Error reading input file: {e}")
        return

    try:
        with open(output_filepath, "w") as output_file:

            output_file.write("EMPLOYEE PAYOUT SUMMARY\n")
            output_file.write("=======================\n")

            for name, total in payouts.items():
                output_file.write(f"{name}: Rs {total:.2f}\n")

        print("\n===== PART B: PROCESSING SUMMARY =====")
        print(f"Unique employees processed: {len(payouts)}")

        for name, total in payouts.items():
            print(f"{name}: Rs {total:.2f}")

        print(f"\nSummary saved to: {output_filepath}")

    except OSError as e:
        print(f"Error writing output file: {e}")


# Main Program

if __name__ == "__main__":
    process_records(
        "Members/Aryan/audit_input.txt",
        "Members/Aryan/audit_summary.txt"
    )
