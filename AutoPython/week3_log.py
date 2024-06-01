import logging

def loggin_check() -> None:
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("This is a DEBUG message.")
    logging.info("This is an INFO message.")
    logging.warning("This is a WARNING message.")
    logging.error("This is an ERROR message.")
    logging.critical("This is a CRITICAL message.")

def handlers():
    stream_log = logging.getLogger("stream_log")
    stream_log.setLevel(logging.DEBUG)
    stream_log.handlers = []
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_log.addHandler(stream_handler)
    stream_log.info("This is Debug")

if __name__ == "__main__":
    # loggin_check()
    handlers()