from abc import ABC, abstractmethod
from khushi_exceptions import CellOverheatError, LowPowerError


class BaseCell(ABC):
    @abstractmethod
    def execute_pulse(self, voltage, temp):
        pass

    @abstractmethod
    def get_status(self):
        pass


class DivyCell(BaseCell):
    def __init__(self, cell_id, **config):
        self.cell_id = cell_id
        self.config = config
        self.current_voltage = config.get("initial_voltage", 100.0)
        self.current_temp = config.get("initial_temp", 25.0)

    def execute_pulse(self, voltage, temp):
        self.current_voltage = voltage
        self.current_temp = temp

        if self.current_temp > 85.0:
            raise CellOverheatError(self.current_temp)

        if self.current_voltage < 15.0:
            raise LowPowerError(self.current_voltage)

        return "Cell " + str(self.cell_id) + " worked fine at " + str(voltage) + "% voltage and " + str(temp) + "°C."

    def get_status(self):
        return {
            "cell_id": self.cell_id,
            "voltage": self.current_voltage,
            "temp": self.current_temp,
            "config": self.config
        }

    def log_telemetry(self, *metrics, **status):
        return {
            "cell_id": self.cell_id,
            "metrics_tuple": metrics,
            "status_dict": status
        }
