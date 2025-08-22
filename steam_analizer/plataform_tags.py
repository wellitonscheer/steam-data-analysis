class PlataformTag:
    def __init__(self, plataform):
        self.plataform = plataform
        self.tags = {}
        self.plataform_ocurrence = 0

    def __str__(self):
        return f"{self.plataform}: {self.tags}"
    
    def add_tag(self, tag):
        self.tags[tag] = self.tags.get(tag, 0) + 1
    
    def process_record(self, record):
        for tag in record["Tags"].split(","):
            self.add_tag(tag)
            self.plataform_ocurrence += 1
    
    def sort_tags(self):
        self.tags = sorted(self.tags.items(), key=lambda x: x[1], reverse=True)
    
    def get_info(self):
        self.sort_tags()
        return {
            "plataform": self.plataform,
            "tags": self.tags,
            "plataform_ocurrence": self.plataform_ocurrence
        }

class PlataformTags:
    def __init__(self):
        self.linux_tags = PlataformTag("Linux")
        self.windows_tags = PlataformTag("Windows")
        self.mac_tags = PlataformTag("Mac")
    
    def process_record(self, record):
        if record["Linux"] == "True":
            self.linux_tags.process_record(record)

        if record["Windows"] == "True":
            self.windows_tags.process_record(record)

        if record["Mac"] == "True":
            self.mac_tags.process_record(record)
    
    def sort_tags(self):
        self.linux_tags.sort_tags()
        self.windows_tags.sort_tags()
        self.mac_tags.sort_tags()
    
    def get_info(self):
        self.sort_tags()
        return {
            "linux_tags": self.linux_tags.get_info(),
            "windows_tags": self.windows_tags.get_info(),
            "mac_tags": self.mac_tags.get_info()
        }
        