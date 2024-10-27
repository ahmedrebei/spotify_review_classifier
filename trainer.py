from models.bert_model import BERTModel
from data.data_loader import DataLoader


class Trainer:
    def __init__(self, model: BERTModel, data_loader: DataLoader, epochs: int, learning_rate: float):
        pass
    
    def train(self):
        pass
    
    def evaluate(self):
        pass
    
    def save_model(self, file_path: str):
        pass
