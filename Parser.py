from Rutube import Rutube
from Youtube import Youtube


class ParserClass:
    def __init__(self, path, link):
        if link.find("rutube"):
            Rutube(path, link)

        elif link.find("youtube"):
            Youtube(path, link)
