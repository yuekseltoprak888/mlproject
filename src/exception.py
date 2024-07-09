import sys
import traceback
import logging
from datetime import datetime
import os


# Configure logging
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='%(asctime)s - %(levelname)s - %(message)s - %(filename)s:%(lineno)d',
    level=logging.INFO
)

def error_message_detail(error, error_detail: sys):
    # Get the exception info
    _, _, exc_tb = sys.exc_info()
    
    # Extract the file name and line number from the traceback
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    
    # Create the error message
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(file_name, line_number, str(error))
    
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
