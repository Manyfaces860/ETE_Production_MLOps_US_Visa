import os, sys, numpy as np
import dill, yaml, pandas as pd

from us_visa.logger import logging
from us_visa.exception import USVisaException

def read_yaml_file(file_path: str) -> dict:
    """
    Reads a YAML file and returns its contents as a dictionary.
    
    Args:
        file_path (str): Path to the YAML file.
        
    Returns:
        dict: Contents of the YAML file.
        
    Raises:
        USVisaException: If the file does not exist or cannot be read.
    """
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError as e:
        raise USVisaException(f"File not found: {file_path}", sys) from e
    except Exception as e:
        raise USVisaException(e, sys) from e


def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
            yaml.dump(content, file)
    except Exception as e:
        raise USVisaException(e, sys) from e
    
def load_object(file_path: str) -> object:
    logging.info("Entered the load_object method of utils")
    try:
        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)
        logging.info("Exited the load_object method of utils")

        return obj
    except Exception as e:
        raise USVisaException(e, sys) from e
    
def save_numpy_array_data(file_path: str, array: np.array) -> None:
    """
    Save numpy array data to file
    file_path: str location of file to save
    array: np.array data to save
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise USVisaException(e, sys) from e
    
def load_numpy_array_data(file_path: str) -> np.array:
    """
    load numpy array data from file
    file_path: str location of file to load
    return: np.array data loaded
    """
    try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise USVisaException(e, sys) from e
    
def save_object(file_path: str, obj: object) -> None:
    """
    Save an object to a file using dill.
    
    Args:
        file_path (str): Path to the file where the object will be saved.
        obj (object): The object to save.
        
    Raises:
        USVisaException: If the file cannot be written.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise USVisaException(e, sys) from e
    
def drop_columns(df: pd.DataFrame, cols: list)-> pd.DataFrame:

    """
    drop the columns form a pandas DataFrame
    df: pandas DataFrame
    cols: list of columns to be dropped
    """
    logging.info("Entered drop_columns methon of utils")

    try:
        df = df.drop(columns=cols, axis=1)

        logging.info("Exited the drop_columns method of utils")
        
        return df
    except Exception as e:
        raise USVisaException(e, sys) from e