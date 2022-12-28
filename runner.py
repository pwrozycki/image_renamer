import logging
import os
from logging import Formatter
from logging.handlers import RotatingFileHandler

from locations import COLLECTION_PHYS_ROOT, collection_walk
from renamer import Renamer
from pidfile import handle_pidfile

LOG_FILE = os.path.join(COLLECTION_PHYS_ROOT, '/tmp/', 'image_renamer.log')


def configure_logging():
    # configure logging
    logger = logging.getLogger()

    logger.setLevel(logging.INFO)

    file_handler = RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=8)
    file_handler.setFormatter(Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    logger.addHandler(file_handler)


if __name__ == '__main__':
    configure_logging()
    handle_pidfile('/tmp/image_renamer.pid')

    for (root, dirs, files) in collection_walk():
        renamed = Renamer(root, files).rename_jpgs_in_collection()
