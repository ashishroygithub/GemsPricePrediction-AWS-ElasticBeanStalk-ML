import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_object

@dataclass
class DataTransformationConfig:
    """ Configuration for Data Transformation including paths for objects and files. """
    preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')


class DataTransformation:
    """ Class responsible for data transformation processes. """

    def __init__(self):
        """ Initialize DataTransformation with its configuration. """
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation_object(self) -> ColumnTransformer:
        """ 
        Setup the data transformation pipeline.

        Returns:
            ColumnTransformer: Preprocessor for data transformation.
        """
        try:
            # Define which columns should be ordinal-encoded and which should be scaled
            categorical_cols = ['cut', 'color','clarity']
            numerical_cols = ['carat', 'depth','table', 'x', 'y', 'z']

            # Define custom ranking for each ordinal variable
            cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']

            # Set up pipeline for numerical features
            num_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler())                
                ]
            )

            # Set up pipeline for categorical features
            cat_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('ordinal_encoder', OrdinalEncoder(categories=[cut_categories, color_categories, clarity_categories])),
                    ('scaler', StandardScaler())
                ]
            )

            logging.info(f'Categorical Columns : {categorical_cols}')
            logging.info(f'Numerical Columns   : {numerical_cols}')

            # Combine both pipelines into a column transformer
            preprocessor = ColumnTransformer(
                transformers=[
                    ('num_pipeline', num_pipeline, numerical_cols),
                    ('cat_pipeline', cat_pipeline, categorical_cols)
                ]
            )

            logging.info('Data transformation pipelines created successfully.')
            return preprocessor
        
        except Exception as e:
            logging.error('Exception occured in Data Transformation Phase: %s', str(e))
            raise CustomException(e, sys)
        
    def initate_data_transformation(self, train_path, test_path) -> tuple:
        """ 
        Handles the process of transforming training and test datasets.

        Args:
            train_path (str): Path to the training dataset.
            test_path (str): Path to the test dataset.

        Returns:
            tuple: Transformed train array, test array and path to saved preprocessor object.
        """
        try:
            # Read train and test data
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info('Successfully read train and test data.')
            logging.info(f'Train Dataframe Head : \n{train_df.head().to_string()}')
            logging.info(f'Test Dataframe Head  : \n{test_df.head().to_string()}')

            # Get the transformation object
            logging.info('Obtaining preprocessing object')
            preprocessing_obj = self.get_data_transformation_object()

            # Set target column name and columns to be dropped
            target_column_name = 'price'
            drop_columns = [target_column_name, 'id']

            # Drop specified columns for training and test datasets
            input_feature_train_df = train_df.drop(columns=drop_columns, axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=drop_columns, axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info("Applying preprocessing object on training and testing datasets.")
            
            # Transform train and test datasets
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]
            
            # Save the transformation object for future use
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            logging.info('Successfully saved preprocessor pickle file.')

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        
        except Exception as e:
            logging.error('Exception occured in initiate_data_transformation function: %s', str(e))
            raise CustomException(e, sys)
