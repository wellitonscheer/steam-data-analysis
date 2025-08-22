import csv
from plataform_tags import PlataformTags

with open("dataset/steam_games.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")

    headers = []
    data = []
    
    plataform_tags = PlataformTags()

    for row in reader:
        if reader.line_num == 1:
            headers = row
            continue

        record = {header: row[i] for i, header in enumerate(headers)}
        data.append(record)

        plataform_tags.process_record(record)

        # if reader.line_num == 10:
        #     break
    
    info = plataform_tags.get_info()
    
    print(info)