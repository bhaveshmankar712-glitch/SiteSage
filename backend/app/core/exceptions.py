class CrawlError(Exception):
    def __init__(self, raised_by):
        self.raised_by = raised_by
        self.message = "Error while crawling the website"
        super().__init__()

    def __str__(self):
        return self.message