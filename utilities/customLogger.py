import logging


class LogGen:

    @staticmethod
    def Loggen():
        '''logging.basicConfig(level=logging.INFO,filename=".//LogGene//caseone.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        #logger.setLevel(logging.INFO)
        # logger.setLevel(logging.ERROR)
        return logger'''


        # Set up the logger
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)  # Set the desired logging level (e.g., INFO, DEBUG)

        # Create a file handler to save logs to a file
        file_handler = logging.FileHandler(".//LogGen//selenium_logs.txt")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger
