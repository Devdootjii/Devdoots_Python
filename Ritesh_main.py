import random 
from Ritesh_cells import DivyCell
from Ritesh_exceptions  import CellOverheatError, LowPowerError
from Ritesh_logger import SwarmLogger, format_percentage

def run_simulation():
    logger = SwarmLogger()

    cell_1 = DivyCell(cell_id="Alpha-1", role="Sensor" , mode="Active")
    cell_2 = DivyCell(cell_id="Beta-2", role="Relay" , mode="standby")

    cells =[cell_1,cell_2]

    print("=== STARTING DAIVY SIMULATOR ===\n")

    for cell in cells:
        print(cell.get_status())

        for cycle in range(1,4):
            temp = random.randint(50,100)
            power = random.uniform(0.05, 1.0)

            cell.log_telemetry(temp, power, cycle=cycle , status="Running")

            try:
                result = cell.execute_pulse(temp,power)
                log_msg = f"[SUCCESS] {result} | Power: {format_percentage(power)}"
                logger.log_event(log_msg)
                print(log_msg)

            except CellOverheatError as e:
                err_msg = f"[CRITICAL ERRROR] {e}"
                logger.log_event(err_msg)
                print(err_msg)

            except LowPowerError as e:
                err_msg =f"[WARNING] {e}"
                logger.log_event(err_msg)
                print(err_msg)

            except Exception as e:
                print(f"[UNKNOWN ERROR] {e}")


    print("-"* 40)

    logger.read_logs()

if __name__ == "__main__":
    run_simulation()                