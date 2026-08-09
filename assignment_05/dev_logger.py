class SwarmLogger:

  def __init__(self, file_path="swarm_telemetry.txt"):
    self.file_path = file_path

  def write_log(self, log_message):  # eite_log -> write_log fix
    with open(self.file_path, "a") as f:
      f.write(log_message + "\n")

  def read_logs(self):
    try:
      with open(self.file_path, "r") as f:
        content = f.read()
        return content
    except FileNotFoundError:
      return "file not found!"


format_percentage = lambda val: f"{val * 100:.1f}%"