from abc import ABC, abstractmethod

class BaseAIModel(ABC):
    @abstractmethod
    def train_model(self, dataset_name):
        pass

    @abstractmethod
    def evaluate_accuracy(self):
        pass

class VisionModel(BaseAIModel):
    def train_model(self, dataset_name):
        return f"Training Computer Vision model on {dataset_name} dataset...."

    def evaluate_accuracy(self):
        return "Vision Model Accuracy: 94.5%"

class NLPModel(BaseAIModel):
    def train_model(self, dataset_name):
        return f"Training NLP model on {dataset_name} dataset...."

    def evaluate_accuracy(self):
        return "NLP Model Accuracy: 88.5%"

print("--task 2--")
vision = VisionModel()
print(vision.train_model("ImageNet"))
print(vision.evaluate_accuracy())

nlp = NLPModel()
print(nlp.train_model("IMDB Reviews"))
print(nlp.evaluate_accuracy())