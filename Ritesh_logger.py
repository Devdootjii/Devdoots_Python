format_percentage = lambda val:f"{val*100:.1f}%"

class SwarmLogger:
    def __init__(self):
        self.filename= "ritesh_swarm_telemetry.txt"

    def log_event(self, message):
        with open(self.filename, "a") as file:
            file.write(message + "\n") 

    def read_logs(self):
        try:
            with open (self.filename,"r") as file:
                print("\n--- Swarm Telemetry Logs ---")
                print(file.read())
        except FileNotFoundError:
            print("LOG ERROR: 'ritesh_swarm_telemetry.txt' File Dosn't created.")
                          