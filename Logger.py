import logging

# Creating logging Config
logging.basicConfig(
    filename= 'forest_fire_log_file.log',
    level= logging.INFO,
    format= '%(asctime)s %(levelname)s - %(message)s',
    datefmt= '%d-%m-%y %H:%M:%S'
)

# Creating Logger Object
log = logging.getLogger()
log.setLevel(logging.DEBUG)