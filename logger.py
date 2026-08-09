# logger.py

# 1-liner lambda for percentage
format_percentage = lambda val: f"{val * 100:.1f}%"

class SwarmLogger:
    def append_log(self, message):
        with open("swarm_telemetry.txt", "a") as file:
            file.write(message + "\n")

    def read_logs(self):
        try:
            with open("swarm_telemetry.txt", "r") as file:
                return file.read()
        except FileNotFoundError:
            return "Error: Log file not found!"