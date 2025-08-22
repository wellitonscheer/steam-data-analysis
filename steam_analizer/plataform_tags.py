class PlataformTag:
    def __init__(self, plataform):
        self.plataform = plataform
        self.tags_ocurrence = {}
        self.plataform_ocurrence = 0

    def __str__(self):
        return f"{self.plataform}: {self.tags_ocurrence}"
    
    def add_tag(self, tag):
        stored_tag = self.tags_ocurrence.get(tag, {"ocurrence": 0, "percent": 0})
        ocurrence = stored_tag["ocurrence"] + 1
        percent = ocurrence / self.plataform_ocurrence
        self.tags_ocurrence[tag] = {"ocurrence": ocurrence, "percent": percent}
    
    def process_tags(self, tags):
        self.plataform_ocurrence += 1

        for tag in tags.split(","):
            tag = tag.strip()
            if not tag:
                continue
            self.add_tag(tag)
    
    def sort_tags(self):
        return sorted(self.tags_ocurrence.items(), key=lambda x: x[1]["ocurrence"], reverse=True)
    
    def get_info(self):
        return {
            "plataform": self.plataform,
            "tags": self.sort_tags()[0:5],
            "plataform_ocurrence": self.plataform_ocurrence,
        }

class PlataformTags:
    def __init__(self):
        self.linux_tags = PlataformTag("Linux")
        self.windows_tags = PlataformTag("Windows")
        self.mac_tags = PlataformTag("Mac")
    
    def process_record(self, record):
        if record.get("Linux") == "True":
            self.linux_tags.process_tags(record.get("Tags", ""))

        if record.get("Windows") == "True":
            self.windows_tags.process_tags(record.get("Tags", ""))

        if record.get("Mac") == "True":
            self.mac_tags.process_tags(record.get("Tags", ""))
    
    def get_info(self):
        return {
            "linux_tags": self.linux_tags.get_info(),
            "windows_tags": self.windows_tags.get_info(),
            "mac_tags": self.mac_tags.get_info()
        }
        