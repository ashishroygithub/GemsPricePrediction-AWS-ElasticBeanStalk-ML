import os
import sys

import numpy as np 
import pandas as pd
import dill
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

from src.exception import CustomException
from src.logger import logging

def save_object(file_path, obj):
    """
    Save a Python object to a specified path using dill.
    
    Parameters:
    - file_path: The path where the object should be saved.
    - obj: The Python object to save.
    """
    try:
        logging.info(f"Saving object to {file_path}...")
        
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

        logging.info(f"Object successfully saved to {file_path}")

    except Exception as e:
        logging.error(f"Failed to save object to {file_path}. Error: {str(e)}")
        raise CustomException(e, sys)

def evaluate_models(xtrain, ytrain, xtest, ytest, models):
    """
    Train and evaluate multiple models on given data.
    
    Parameters:
    - xtrain, ytrain: Training data and labels.
    - xtest, ytest: Testing data and labels.
    - models: A dictionary containing model names as keys and model instances as values.

    Returns:
    - report: A dictionary containing model names as keys and their R2 scores on test data as values.
    """
    report = {}
    try:
        for i in range(len(models)):
            model_name = list(models.keys())[i]
            model = list(models.values())[i]
            
            logging.info(f"Training {model_name}...")

            model.fit(xtrain, ytrain)
            logging.info(f"{model_name} trained successfully.")

            y_train_pred = model.predict(xtrain)
            y_test_pred = model.predict(xtest)

            test_model_score = r2_score(ytest, y_test_pred)
            report[model_name] =  test_model_score

        logging.info("All models evaluated successfully.")
        return report

    except Exception as e:
        logging.error(f"Exception occured during model training. Error: {str(e)}")
        raise CustomException(e, sys)

def model_metrics(true, predicted):
    """
    Calculate various regression metrics for model evaluation.
    
    Parameters:
    - true: Array of true target values.
    - predicted: Array of predicted target values by a model.

    Returns:
    - mae, rmse, r2_square: Mean Absolute Error, Root Mean Squared Error, and R2 score, respectively.
    """
    try:
        mae = mean_absolute_error(true, predicted)
        mse = mean_squared_error(true, predicted)
        rmse = np.sqrt(mse)
        r2_square = r2_score(true, predicted)
        return mae, rmse, r2_square
    except Exception as e:
        logging.error(f"Exception occured while evaluating metrics. Error: {str(e)}")
        raise CustomException(e, sys)

def print_evaluated_results(xtrain, ytrain, xtest, ytest, model):
    """
    Print evaluation metrics of a trained model on training and test data.
    
    Parameters:
    - xtrain, ytrain: Training data and labels.
    - xtest, ytest: Testing data and labels.
    - model: The trained model to evaluate.
    """
    try:
        logging.info("Printing evaluation results...")

        ytrain_pred = model.predict(xtrain)
        ytest_pred = model.predict(xtest)

        model_train_mae , model_train_rmse, model_train_r2 = model_metrics(ytrain, ytrain_pred)
        model_test_mae , model_test_rmse, model_test_r2 = model_metrics(ytest, ytest_pred)

        print('Model performance for Training set')
        print("- Root Mean Squared Error: {:.4f}".format(model_train_rmse))
        print("- Mean Absolute Error: {:.4f}".format(model_train_mae))
        print("- R2 Score: {:.4f}".format(model_train_r2))

        print('----------------------------------')
    
        print('Model performance for Test set')
        print("- Root Mean Squared Error: {:.4f}".format(model_test_rmse))
        print("- Mean Absolute Error: {:.4f}".format(model_test_mae))
        print("- R2 Score: {:.4f}".format(model_test_r2))
    
        logging.info("Evaluation results printed successfully.")
    
    except Exception as e:
        logging.error(f"Exception occured during printing of evaluated results. Error: {str(e)}")
        raise CustomException(e, sys)
    
def load_object(file_path):
    """
    Load a Python object from a specified path using dill.
    
    Parameters:
    - file_path: The path where the object is saved.

    Returns:
    - The loaded Python object.
    """
    try:
        logging.info(f"Loading object from {file_path}...")

        with open(file_path, 'rb') as file_obj:
            obj = dill.load(file_obj)

        logging.info(f"Object successfully loaded from {file_path}.")
        return obj

    except Exception as e:
        logging.error(f"Failed to load object from {file_path}. Error: {str(e)}")
        raise CustomException(e, sys)
