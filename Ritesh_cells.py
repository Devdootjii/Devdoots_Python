from abc import ABC, abstractmethod
from Ritesh_exceptions import CellOverheatError, LowPowerError

class BaseCell(ABC):
    @abstractmethod
    def execute_pulse(self, temp , power):
        pass
    @abstractmethod
    def get_status(self):
        pass

class DivyCell(BaseCell):
    def __init__(self, cell_id, **config):
        self.cell_id = cell_id
        self.config = config

    def log_telemetry(self ,*metrics, **status):
        print(f"[{self.cell_id}] Metrics: {metrics} | Status: {status}")

    def execute_pulse(self , temp , power):
        if temp > 85 :
            raise CellOverheatError(f"Cell {self.cell_id} Overheated at {temp} .^C")
        if power < 0.15 :
            raise LowPowerError(f"cell {self.cell_id} Low Power at {power*100}%")
        return f"Cell {self.cell_id} pulse executed safely ."

    def get_status(self):
        return f"cell {self.cell_id} is active with self.config: {self.config}"
    

    
                                
                                