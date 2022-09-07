import sys
from customer_personality.components.stage_00_data_ingestion import DataIngestion
from customer_personality.components.stage_01_data_validation import DataValidation
from customer_personality.components.stage_02_data_transformation import DataTransformation
from customer_personality.components.stage_03_model_trainer import ModelTrainer
from customer_personality.exception.exception_handler import AppException

class TrainingPipeline:
    def __init__(self):
        try:
            self.data_ingestion = DataIngestion()
            self.data_validation = DataValidation()
            self.data_transformation = DataTransformation()
            self.model_trainer = ModelTrainer()
        except Exception as e:
            raise AppException(e, sys) from e
     

    def start_training_pipeline(self):
        """
        Starts the training pipeline
        :return: none
        """
        try:
            self.data_ingestion.initiate_data_ingestion()
            self.data_validation.initiate_data_validation()
            self.data_transformation.initiate_data_transformation()
            self.model_trainer.initiate_model_trainer()
        except Exception as e:
            raise AppException(e, sys) from e
