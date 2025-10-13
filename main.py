import logging
# 1
logging.basicConfig(level=logging.DEBUG)

logging.debug("DEBUG message for developers")
logging.info("INFO message, plain information")
logging.warning("WARNING message, something gone wrong")
logging.error("ERROR message, something broke")
logging.critical("CRITICAL message, program cannot run further")

# 2
logging.basicConfig(
   filename="app.log",
   level=logging.DEBUG,
   format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Program is running")
logging.error("Something went wrong")

# 3
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

logger.debug("debug message")
logger.info("info message")

#4
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("app.log", encoding="utf-8")

file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)
logger.debug("DEBUG")
logger.info("INFO")
logger.warning("WARNING")
logger.error("ERROR")
logger.critical("CRITICAL")
