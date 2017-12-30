"""Contains class Application."""
import logging

LOGGER = logging.getLogger(__name__)


class Application(object):
    """Application is the class entry point to run current application."""

    def start(self):
        """Start the application."""
        LOGGER.info("Starting application")
        raise NotImplementedError
