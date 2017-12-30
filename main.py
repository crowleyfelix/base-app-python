"""Module with entry point."""
import logging
from app import logger
from app.application import Application

LOGGER = logging.getLogger(__name__)


def main():
    """Application entry point."""
    logger.setup()
    app = Application()

    try:
        app.start()
    except KeyboardInterrupt:
        logging.debug("Stopping gracefully")


if __name__ == "__main__":
    main()
