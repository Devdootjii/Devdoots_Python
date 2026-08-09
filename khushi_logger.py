import os

format_percentage = lambda value: f"{value * 100:.1f}%"


class SwarmLogger:
    def __init__(self, log_file="swarm_telemetry.txt"):
        self.log_file = log_file

    def log_event(self, level, message):
        with open(self.log_file, "a") as file:
            file.write(f"[{level}] {message}\n")

    def read_logs(self):
        try:
            if not os.path.exists(self.log_file):
                raise FileNotFoundError(f"Log file '{self.log_file}' was not found.")
            with open(self.log_file, "r") as file:
                logs = file.readlines()
            return [line.strip() for line in logs]
        except FileNotFoundError as error:
            print(f"[LOGGER ERROR]: {error}")
            return []

    def filter_critical_warnings(self):
        logs = self.read_logs()
        return list(filter(lambda line: "CRITICAL" in line or "WARNING" in line, logs)) 