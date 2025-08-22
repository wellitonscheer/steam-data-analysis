import csv
from plataform_tags import PlataformTags

class SteamAnalizer:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.data = []
        self.plataform_tags = PlataformTags()
    
    def process_csv(self):
        """
        processa o arquivo csv e carrega os dados em uma lista
        """
        with open(self.csv_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")

            headers = []
            for row in reader:
                if reader.line_num == 1:
                    headers = row
                    continue

                record = {header: row[i] for i, header in enumerate(headers)}
                self.data.append(record)

    def process_data(self):
        """
        processa todos os registros para todas as funcionalidades do analizador
        """
        for record in self.data:
            self.plataform_tags.process_record(record)
    
    def process_plataform_tags(self, record=None):
        """
        processa um registro ou todos os registros
        """
        if record:
            self.plataform_tags.process_record(record)
            return

        for record in self.data:
            self.plataform_tags.process_record(record)