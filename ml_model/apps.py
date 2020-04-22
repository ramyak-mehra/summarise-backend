from django.apps import AppConfig
import nltk

class MlModelConfig(AppConfig):
    name = 'ml_model'
    def ready(self):
        nltk.download()
    
