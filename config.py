import json
import os


class Config:
    def __init__(self, config_file: str = "config.json"):
        self.config = self.load_config(config_file)

    def load_config(self, config_file: str):
        # Load configuration from a JSON file
        if os.path.exists(config_file):
            with open(config_file, 'r') as file:
                return json.load(file)
        else:
            raise FileNotFoundError(f"Configuration file {config_file} not found.")

    @staticmethod
    def get_training_config():
        return {
            "batch_size": 32,
            "learning_rate": 0.001,
            "epochs": 10
        }

    @staticmethod
    def get_model_config():
        return {
            "model_name": "bert-base-uncased",
            "max_seq_length": 128
        }
