class SwarmError(Exception):
    pass


class CellOverheatError(SwarmError):
    def __init__(self, temp):
        self.temp = temp
        super().__init__(f"CRITICAL OVERHEAT WARNING: Cell temperature reached {temp}°C (Exceeds limit of 85°C)!")


class LowPowerError(SwarmError):
    def __init__(self, charge):
        self.charge = charge
        super().__init__(f"LOW POWER WARNING: Battery level dropped to {charge}% (Below minimum 15%)!")


def check_system(temp, charge):
    if temp > 85:
        raise CellOverheatError(temp)
    if charge < 15:
        raise LowPowerError(charge)


try:
    check_system(90, 10)
except SwarmError as error:
    print(error)