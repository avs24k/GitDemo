import logging


class classname:
    def getlogs(self):
        logger = logging.getLogger()
        filehandler = logging.FileHandler("file.log",mode="w")

        formatter =logging.Formatter("%(asctime)s: %(levelname)s: %(module)s: %(name)s: %(message)s")

        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger