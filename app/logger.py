"""Creates a root logger."""
import logging


LOG_FORMAT = "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"
DATETIME_FORMAT = "%m-%d %H:%M"


def setup():
    """Build logging engine."""
    logging.basicConfig(level=logging.DEBUG,
                        format=LOG_FORMAT,
                        datefmt=DATETIME_FORMAT)
