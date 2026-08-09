# Task 1:custom exception hierarchy

class Exception:
    pass
class SwaemError(Exception):
    pass
class CelloverheatError(SwaemError):
    def __init__(self,cell_id,temperature):
        sef.cell_id=cell_id
        self.temperature=temperature
        super().__init__(message)
        return f"Cell{cell_id} Temperature{temperature}C excuds limit!"
        class lowpowererror(SwaemError):
            def __init__(self,cell_id,power_level):
                self.cell_id=cell_id
                self.power_level=power_level
                super().__init__(message)
                return f"Cell{cell_id} Power{power_level}% is below threshold!"
