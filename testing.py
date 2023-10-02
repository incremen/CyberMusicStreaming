from custom_logging import CustomLogger
import logging

testing_logger = CustomLogger(log_files=["testing.log"])

logging.info(f"{bool([])=}")