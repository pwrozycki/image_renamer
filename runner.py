import logging
import os
from logging import Formatter
from logging.handlers import RotatingFileHandler

from locations import COLLECTION_PHYS_ROOT, collection_walk
from renamer import Renamer

LOG_FILE = os.path.join(COLLECTION_PHYS_ROOT, '/tmp/', 'renamer.log')


def configure_logging():
    # configure logging
    logger = logging.getLogger()

    logger.setLevel(logging.INFO)

    file_handler = RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=8)
    file_handler.setFormatter(Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    logger.addHandler(file_handler)


if __name__ == '__main__':
    configure_logging()

    for (root, dirs, files) in collection_walk():
        renamed = Renamer(root, files).rename_jpgs_in_collection()
