from TTS.utils.manage import ModelManager

# Create an instance of ModelManager
model_manager = ModelManager()

# List available models
models = model_manager.list_models()
print("Available models:", models)
