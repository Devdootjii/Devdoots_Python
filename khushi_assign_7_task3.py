class MiniDAIVY:
    def __init__(self, bot_name):
        self.bot_name = bot_name
        self.battery = 100
        self.energy = 100
        self.mood = "HAPPY"

    def do_task(self, task_name):
        if self.battery <= 10:
            print(" System low! please charge MiniDAIVY")
        else: 
            print("system perform all task")
            self.energy = self.energy - 20
            self.battery = self.battery - 15
    def charge_battery(self):
        self.battery = 100     
    def get_status(self): 
        print("Bot name:", self.bot_name)
        print("Battery:", self.battery)
        print("energy:", self.energy)
        print("Mood:", self.mood)

robot = MiniDAIVY("MiniDAIVY")  
robot.do_task("cleaning")  
robot.get_status()

robot.charge_battery()
robot.get_status()
               