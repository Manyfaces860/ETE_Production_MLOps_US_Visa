import os, sys

def get_detailed_error_message(error_message, error_detail: sys):
    """
    :param error_message: error message in string format
    :param error_detail: error details in sys module
    :return: formatted error message
    """
    
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    
    formatted_error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] with error message: [{error_message}]"
    
    return formatted_error_message

class USVisaException(Exception):
    def __init__(self, error_message, error_detail: sys):
        """
        :param error_message: error message in string format
        """
        
        super().__init__(error_message)
        self.error_message = USVisaException.get_detailed_error_message(str(error_message), error_detail)
        
    def __str__(self):
        return self.error_message