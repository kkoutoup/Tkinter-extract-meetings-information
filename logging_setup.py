# Python modules
import logging

# set up logging
logging.basicConfig(filename='meetings_report.log', format='%(asctime)s-%(levelname)s\n%(message)s', datefmt='%d/%m/%Y @ %H:%M:%S', filemode='w', level=logging.INFO)