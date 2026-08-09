import random
from cells import DivyCell
from logger import SwarmLogger, format_percentage
from exceptions import CellOverheatError, LowPowerError, SwarmError


def run_simulation():
    print("-- DEVDOOTS SWARM CAPSTONE SIMULATION --")

    logger = SwarmLogger("swarm_telemetry.txt")

    cells = [
        DivyCell(
            cell_id=f"DC-00{i}",
            initial_voltage=random.uniform(50, 100),
            initial_temp=random.uniform(25, 40)
        )
        for i in range(1, 4)
    ]

    logger.log_event("INFO", f"Initialized {len(cells)} DivyCells successfully.")

    for cycle in range(1, 6):
        print(f"\n-- Simulation Cycle {cycle} --")

        for cell in cells:
            sim_voltage = random.uniform(5, 100)
            sim_temp = random.uniform(20, 95)

            try:
                cell.execute_pulse(sim_voltage, sim_temp)

                status_msg = f"{cell.cell_id}: Normal Ops - V: {sim_voltage:.1f}%, T: {sim_temp:.1f}°C"
                print(f"[SUCCESS] {status_msg}")
                logger.log_event("INFO", status_msg)

                cell.log_telemetry(sim_voltage, sim_temp, status="HEALTHY", cycle=cycle)

            except CellOverheatError as error:
                err_msg = f"{cell.cell_id} OVERHEAT -> {error}"
                print(f"[CRITICAL EXCEPTION] {err_msg}")
                logger.log_event("CRITICAL", err_msg)

            except LowPowerError as error:
                err_msg = f"{cell.cell_id} LOW POWER -> {error}"
                print(f"[WARNING EXCEPTION] {err_msg}")
                logger.log_event("WARNING", err_msg)

            except SwarmError as error:
                err_msg = f"{cell.cell_id} GENERAL SWARM ERROR -> {error}"
                print(f"[ERROR] {err_msg}")
                logger.log_event("ERROR", err_msg)

    test_ratio = 0.854
    print(f"\n[LAMBDA DEMO] Telemetry Ratio {test_ratio} formatted: {format_percentage(test_ratio)}")

    print("\n-- CRITICAL LOGS FILTERED FROM FILE --")
    critical_logs = logger.filter_critical_warnings()

    for log in critical_logs:
        print(f" -> {log}")


if __name__ == "__main__":
    run_simulation()
