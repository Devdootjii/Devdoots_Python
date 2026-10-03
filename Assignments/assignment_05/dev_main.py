from dev_cells import DivyCell
from dev_exceptions import CellOverheatError, LowPowerError
from dev_logger import SwarmLogger, format_percentage
logger = SwarmLogger()

cell1 = DivyCell("CELL_01", EAP_material="Carbon", battery_type="SolidState")

simulated_sensor_data = [
    {"temp": 45, "voltage": 0.85},  
    {"temp": 90, "voltage": 0.80},  
    {"temp": 50, "voltage": 0.10},  
]

for idx, data in enumerate(simulated_sensor_data):
  try:
    print(cell1.execute_pulse())

    v_perc = format_percentage(data["voltage"])

    if data["temp"] > 85:
      raise CellOverheatError(data["temp"])

    if data["voltage"] < 0.15:
      raise LowPowerError(v_perc)

    log_msg = cell1.log_telemetry(
        f"Temp:{data['temp']}C", status="OPERATIONAL"
    )
    logger.write_log(f"[SUCCESS] {log_msg}")

  except CellOverheatError as e:
    err_msg = f"[CRITICAL ERROR] {e}"
    print(err_msg)
    logger.write_log(err_msg)  

  except LowPowerError as e:
    err_msg = f"[WARNING ERROR] {e}"
    print(err_msg)
    logger.write_log(err_msg)

print("\n--- FINAL SWARM TELEMETRY LOGS ---")
print(logger.read_logs())