class SwarmError(Exception):
    pass

class CellOverheatError(SwarmError):
    def __init__(self , message="CRITICAL : Cell temperature exceeded 85°C!"):
        super().__init__(message)

class LowPowerError(SwarmError):
    def __init__(self, message="WARNING :Battery voltage dropped below 15%!"):
        super().__init__(message)

