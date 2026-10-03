# exceptions.py

# base exception
class SwarmError(Exception):
    pass

# overheat error
class CellOverheatError(SwarmError):
    def __init__(self, message="Cell temp exceeded 85C!"):
        super().__init__(message)

# low power error
class LowPowerError(SwarmError):
    def __init__(self, message="Battery dropped below 15%!"):
        super().__init__(message)