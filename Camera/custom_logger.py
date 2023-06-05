import logging
import sys

class CustomLogger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        self.formatter = logging.Formatter('[%(levelname)s]\t%(asctime)s\t%(message)s',
                                           datefmt='%Y-%m-%d %H:%M:%S')
        
        self.error_handler = logging.FileHandler('error.log')
        self.error_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.error_handler)
        
        self.info_handler = logging.FileHandler('info.log')
        self.info_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.info_handler)
        
        self.stdout_handler = logging.StreamHandler(sys.stdout)
        self.stdout_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.stdout_handler)

    def log_error(self, errormsg):
        self.logger.error(errormsg)
        
    def log_info(self, infomsg):
        self.logger.info(infomsg)
