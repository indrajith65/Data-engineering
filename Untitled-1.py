import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

logger = logging.getLogger(__name__)


def main():
    logger.info("Starting application")
    try:
        logger.info("Doing some work...")
        # application logic here
    except Exception:
        logger.exception("Unhandled exception")
    logger.info("Shutting down")


if __name__ == '__main__':
    main()
