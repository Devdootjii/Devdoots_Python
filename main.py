# main.py
import random
from exceptions import CellOverheatError, LowPowerError
from cells import DivyCell
from logger import SwarmLogger, format_percentage

def run_simulation():
    logger = SwarmLogger()
    cell = DivyCell("Dev-Cell-1", mode="auto", version="v2")
    
    # 5 test cycles
    for i in range(5):
        temp = random.randint(70, 95)
        power = random.uniform(0.05, 0.50)
        
        try:
            p_str = format_percentage(power)
            log = cell.log_telemetry(temp, p_str, active=True)
            logger.append_log(log)
            print(log)
            
            # threshold checks
            if temp > 85:
                raise CellOverheatError(f"Temp High: {temp}C")
            if power < 0.15:
                raise LowPowerError(f"Power Low: {p_str}")
                
            print(cell.execute_pulse())
            
        except CellOverheatError as e:
            print(f"Warning: {e}")
        except LowPowerError as e:
            print(f"Warning: {e}")

    print("\n--- Final Logs ---")
    print(logger.read_logs())

if __name__ == "__main__":
    run_simulation()