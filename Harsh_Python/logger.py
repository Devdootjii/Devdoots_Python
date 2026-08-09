# logger.py

class SwarmLogger:
    def __init__(self, log_file="swarm_telemetry.txt"):
        self.log_file = log_file

    def write_log(self, log_msg):
        with open(self.log_file, "a") as file:
            file.write(f"{log_msg}\n")

    def read_log(self):
        try:
            with open(self.log_file, "r") as file:
                content = file.read()
                print(content)
            return "File Successfully Read."
        except FileNotFoundError:
            return "Log File Not Found Yet."

format_percentage = lambda val: f"{val * 100:.1f}%"


format_percentage = lambda val: f"{val * 100:.1f}%"
print(format_percentage(0.85))   
print(format_percentage(0.142))  
