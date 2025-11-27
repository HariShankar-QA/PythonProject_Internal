import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger("automation")
        logger.setLevel(logging.INFO)

        # Create folder if not exists
        log_dir = "Logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        log_file = os.path.join(log_dir, "automation.log")

        # Avoid duplicate handlers
        if not logger.handlers:
            file_handler = logging.FileHandler(log_file, mode='a')
            formatter = logging.Formatter(
                "%(asctime)s: %(levelname)s: %(message)s",
                "%m/%d/%Y %I:%M:%S %p"
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger
