class MiniDaIVY:
    def __init__(self, bot_name):
        self.bot_name = bot_name
        self.energy = 100
        self.battery = 100
        self.mood = "HAPPY"

    def do_task(self, task_name):
        if self.battery <= 10:
            print("System Low! Please charge Mini-DAIVY.")
            return

        self.energy -= 20
        self.battery -= 15

        print(f"{self.bot_name} completed: {task_name}")

    def charge_battery(self):
        self.battery = 100
        print("Battery charged to 100%")

    def get_status(self):
        print(f"Bot Name: {self.bot_name}")
        print(f"Energy: {self.energy}")
        print(f"Battery: {self.battery}")
        print(f"Mood: {self.mood}")

bot = MiniDaIVY("DAIVY")
bot.get_status()
bot.do_task("Scanning System")
bot.get_status()
bot.charge_battery()
bot.get_status()
    
