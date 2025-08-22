class PlataformTags:
    def __init__(self):
        self.linux_tags = {}
        self.windows_tags = {}
        self.mac_tags = {}
    
    def process_record(self, record):
        if record["Linux"] == "True":
            for tag in record["Tags"].split(","):
                self.linux_tags[tag] = self.linux_tags.get(tag, 0) + 1

        if record["Windows"] == "True":
            for tag in record["Tags"].split(","):
                self.windows_tags[tag] = self.windows_tags.get(tag, 0) + 1

        if record["Mac"] == "True":
            for tag in record["Tags"].split(","):
                self.mac_tags[tag] = self.mac_tags.get(tag, 0) + 1
    
    def sort_tags(self):
        self.linux_tags = sorted(self.linux_tags.items(), key=lambda x: x[1], reverse=True)
        self.windows_tags = sorted(self.windows_tags.items(), key=lambda x: x[1], reverse=True)
        self.mac_tags = sorted(self.mac_tags.items(), key=lambda x: x[1], reverse=True)
    
    def get_info(self):
        self.sort_tags()
        return {
            "linux_tags": self.linux_tags[:10],
            "windows_tags": self.windows_tags[:10],
            "mac_tags": self.mac_tags[:10]
        }
        