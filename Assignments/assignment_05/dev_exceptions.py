class SwarmError(Exception):
  pass


class CellOverheatError(SwarmError):

  def __init__(self, temp):
    self.temp = temp
    # __init__ ke baad trailing __ fix kar diya hai
    super().__init__(
        f"Critical Alert: Cell Temperature {temp}°C exceeds 85°C!"
    )


class LowPowerError(SwarmError):

  def __init__(self, voltage):
    self.voltage = voltage
    super().__init__(f"Power Warning: Low Battery Voltage at {voltage}V!")