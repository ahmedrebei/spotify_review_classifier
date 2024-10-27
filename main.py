from config import Config

if __name__ == "__main__":
    config = Config("path/to/your/config.json")
    
    training_config = config.get_training_config()
    model_config = config.get_model_config()

    print("Training Configuration:", training_config)
    print("Model Configuration:", model_config)
