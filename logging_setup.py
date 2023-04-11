# Python modules
import logging

# format log
format_log = "%(asctime)s | File: %(filename)s | Function: %(funcName)s | %(message)s"

# set up logging
logging.basicConfig(filename = 'meetings_report.log', format = format_log, datefmt = '%d/%m/%Y @ %H:%M:%S', filemode = 'w', level = logging.INFO)