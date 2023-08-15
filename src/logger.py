import logging 
import os
from datetime import datetime

# Generate a unique log file name using the current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Construct the path for the logs directory within the current working directory
# It seems there's a small error here as the log file name is being added to the directory path.
# Ideally, you'd want to separate the directory and file name, but I'm leaving it unchanged as per the instruction.
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Ensure the logs directory exists. If it doesn't, create it.
# The exist_ok=True ensures that an error is not raised if the directory already exists.
os.makedirs(logs_path, exist_ok=True)

# Construct the complete log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the built-in Python logging module
logging.basicConfig(
    # Specifies the file where the logs will be written to
    filename=LOG_FILE_PATH,
    
    # Format for the log message
    # asctime: The time the log message was created
    # lineno: The line number in the code where the log message was added
    # name: The name of the logger
    # levelname: The severity level of the log
    # message: The actual log message
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    
    # Set the minimum logging level to INFO. This means messages with level INFO and above 
    # (WARNING, ERROR, etc.) will be logged, but DEBUG messages will be ignored.
    level=logging.INFO
)

"""
This module configures the logging mechanism for the application. 
Logs are saved in a 'logs' directory within the current working directory. 
Each log file is uniquely named based on the timestamp of its creation. 
The logging level is set to 'INFO', and the log messages are formatted to provide 
details about the time, code line number, logger name, log level, and the actual message.
"""
