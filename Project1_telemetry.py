from abc import ABC,abstractmethod 
class Baselogger(ABC):
    @abstractmethod
    def log_data(self,*metrics,**metadata):
        pass
class FileLogger(Baselogger):
    def __init__(self,filename="telemetry.txt"):
        self.filename=filename

    def log_data(self, *metrics, **metadata):
        content=f"metrics : {metrics} | config:{metadata}\n"
        with open(self.filename,"a") as file:
            file.write(content)
    def read_logs(self):
        try:
            with open(self.filename,"r") as file:
                cont = file.read()
                return cont
        except FileNotFoundError:
            return f"file does not exist!"
dev=FileLogger()
dev.log_data("accuracy", "loss", "volatage", lr=0.01, status="online")
print(dev.read_logs())