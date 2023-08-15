# Import all the required libraries
import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# Importing custom exceptions, logging, and other components
from src.exception import CustomException
from src.logger import logging
from src.components.data_transformation import DataTransformation, DataTransformationConfig
from src.components.model_trainer import ModelTrainer, ModelTrainerConfig

# Initialize Data Ingestion Configuration using dataclass for type hinting and cleaner initialization
@dataclass
class DataIngestionConfig:
    """ Configuration for Data Ingestion paths. """
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')


class DataIngestion:
    """ Handles Data Ingestion processes. """

    def __init__(self):
        """ Initialize DataIngestion with its configuration. """
        self.ingestion_config = DataIngestionConfig()

    def initate_data_ingestion(self) -> tuple:
        """ 
        Reads data, splits it, and saves train & test data to specified paths.

        Returns:
            tuple: Paths of the saved train and test datasets.
        """
        logging.info('Data ingestion method Started')

        try:
            # Read data from the specified path
            df = pd.read_csv('notebook/data/gemstone.csv')
            logging.info('Dataset read as pandas Dataframe')

            # Save raw data to the configured path
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info('Raw data saved to %s', self.ingestion_config.raw_data_path)

            # Splitting the data into training and testing sets
            logging.info('Train Test Split Initiated')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save the train and test data to their respective paths
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info('Train data saved to %s and Test data saved to %s', self.ingestion_config.train_data_path, self.ingestion_config.test_data_path)

            logging.info('Ingestion of Data is completed')
            return (self.ingestion_config.train_data_path, self.ingestion_config.test_data_path)

        except Exception as e:
            logging.error('Exception occured at Data Ingestion stage: %s', str(e))
            raise CustomException(e, sys)


# Main driver of the script
if __name__ == '__main__':
    # Start Data Ingestion
    obj = DataIngestion()
    train_data, test_data = obj.initate_data_ingestion()

    # Start Data Transformation
    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initate_data_transformation(train_data, test_data)
    logging.info('Data Transformation completed successfully')

    # Start Model Training
    modeltrainer = ModelTrainer()
    modeltrainer.initiate_model_training(train_arr, test_arr)
    logging.info('Model training completed successfully')
