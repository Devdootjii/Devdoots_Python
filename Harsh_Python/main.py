# main.py
import random
from exceptions import SwarmError, CellOverheatError, LowPowerError
from cells import DivyCell
from logger import SwarmLogger, format_percentage

def run_simulation():
    logger = SwarmLogger()
    
    cells = [
        DivyCell("CELL-01", firmware="v1.0", mode="ACTIVE"),
        DivyCell("CELL-02", firmware="v1.1", mode="STANDBY"),
        DivyCell("CELL-03", firmware="v2.0", mode="ACTIVE")
    ]

    print("Starting DAIVY Swarm Telemetry \n")
 
    for cycle in range(1, 4):
        print(f" Simulation Cycle {cycle}")
        for cell in cells:
            try:

                temp = random.randint(30, 95)               
                power_ratio = random.uniform(0.05, 0.95)         
                power_pct_str = format_percentage(power_ratio)
                power_pct_num = power_ratio * 100

                telemetry = cell.log_telemetry(temp, power_pct_str, mode="RUNNING")
                print(telemetry)
                logger.write_log(f"Cycle {cycle} | {telemetry}")

                if temp > 85:
                    raise CellOverheatError(cell.cell_id, temp)
                if power_pct_num < 15:
                    raise LowPowerError(cell.cell_id, round(power_pct_num, 1))

                print(cell.execute_pulse())

            except CellOverheatError as e:
                error_msg = f"[HANDLED ERROR] {e}"
                print(error_msg)
                logger.write_log(error_msg)

            except LowPowerError as e:
                error_msg = f"[HANDLED ERROR] {e}"
                print(error_msg)
                logger.write_log(error_msg)

            except SwarmError as e:
                error_msg = f"[SWARM ERROR] {e}"
                print(error_msg)
                logger.write_log(error_msg)

            print("-" * 55)

    print("\n=== Reading All Logged Telemetry Files ===")
    logger.read_log()


if __name__ == "__main__":
    run_simulation()
