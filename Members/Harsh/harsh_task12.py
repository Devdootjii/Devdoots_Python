def process_records(input_filepath, output_filepath):
    # Read input file (handle missing file gracefully)
    try:
        with open(input_filepath, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: {input_filepath} not found. Nothing to process.")
        return

    totals = {}

    # Process each line; bad records are logged and skipped
    for line in lines:
        if not line.strip():
            continue
        try:
            parts = line.strip().split(",")
            name = parts[0]
            hours = float(parts[1])
            rate = float(parts[2])

            if hours < 0 or rate < 0:
                raise ValueError("negative value not allowed")

            totals[name] = totals.get(name, 0) + (hours * rate)
        except (IndexError, ValueError) as e:
            print(f"Skipping bad record: '{line.strip()}' ({e})")
            continue

    # Write clean summary report
    with open(output_filepath, "w", encoding="utf-8") as file:
        for name, payout in totals.items():
            file.write(f"{name}: ₹{payout}\n")

    print(f"Summary written to {output_filepath}")


# Sample input with 3 intentional bad records (missing field, bad rate, negative)
sample_data = (
    "Aman,40,250\n"
    "Riya,35,300\n"
    "Corrupt1,40\n"
    "BadRate,ten,200\n"
    "Negative,-5,100\n"
    "Aman,10,250\n"
)

with open("audit_input.txt", "w", encoding="utf-8") as file:
    file.write(sample_data)

process_records("audit_input.txt", "audit_summary.txt")
