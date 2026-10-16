"""
--- PART A: DRY RUN & PREDICTION CHALLENGE ---

def audit_ledger(data, factor=2):
    try:
        data.append(data[-1] * factor)
    except IndexError:
        return "Empty"
    except Exception as e:
        return f"Err: {e}"
    else:
        return data

Predictions & Reasons:
1. Scenario: audit_ledger([10, 20])
   Output: [10, 20, 40]
   Kyun: data[-1] is 20. 20 * 2 = 40. append() mutate karta hai list ko. No error, else block data return karega.

2. Scenario: audit_ledger([])
   Output: "Empty"
   Kyun: data[-1] pe IndexError throw hoga kyunki list empty hai. Except block "Empty" return karega.

3. Scenario: audit_ledger([5, "10"])
   Output: [5, '10', '1010']
   Kyun: data[-1] is string "10". Python me string * 2 sequence repetition karta hai ("1010"). Error nahi aayega, else block execute hoga.
"""

# --- PART B: INTEGRATED AUDIT PIPELINE ---

def process_records(input_file="audit_input.txt", output_file="audit_summary.txt"):
    payout_records = {}

    # File reading with exception control
    try:
        with open(input_file, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File '{input_file}' nahi mili.")
        return

    # Processing lines
    for line_no, line in enumerate(lines, start=1):
        clean_line = line.strip()
        if not clean_line:
            continue

        parts = clean_line.split(",")

        try:
            if len(parts) != 3:
                raise IndexError("Field missing ya extra hai")

            name = parts[0].strip()
            hours = float(parts[1].strip())
            rate = float(parts[2].strip())

            if hours < 0 or rate < 0:
                raise ValueError("Negative values allowed nahi hain")

            total_payout = hours * rate
            payout_records[name] = payout_records.get(name, 0.0) + total_payout

        except (ValueError, IndexError) as err:
            print(f"Skipping line {line_no} [{clean_line}]: {err}")

    # Summary file write karna
    with open(output_file, "w") as out:
        for name, amount in payout_records.items():
            out.write(f"{name}: ₹{amount:.2f}\n")

    # Console output
    print(f"\nProcessing complete. Summary saved to '{output_file}':")
    for name, amount in payout_records.items():
        print(f"- {name}: ₹{amount:.2f}")


# --- Proof of Work (PoW) Test Block ---
if __name__ == "__main__":
    process_records()