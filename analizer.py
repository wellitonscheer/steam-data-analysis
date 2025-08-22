import csv

with open("dataset/steam_games.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")

    headers = []
    data = []
    info = {
        "linux_tags": {},
        "windows_tags": {},
        "mac_tags": {}
    }

    for row in reader:
        if reader.line_num == 1:
            headers = row
            print(headers)
            continue

        record = {header: row[i] for i, header in enumerate(headers)}
        data.append(record)

        if record["Linux"] == "True":
            for tag in record["Tags"].split(","):
                info["linux_tags"][tag] = info["linux_tags"].get(tag, 0) + 1

        if record["Windows"] == "True":
            for tag in record["Tags"].split(","):
                info["windows_tags"][tag] = info["windows_tags"].get(tag, 0) + 1

        if record["Mac"] == "True":
            for tag in record["Tags"].split(","):
                info["mac_tags"][tag] = info["mac_tags"].get(tag, 0) + 1

        # if reader.line_num == 200:
        #     break
    
    info["linux_tags"] = sorted(info["linux_tags"].items(), key=lambda x: x[1], reverse=True)
    info["windows_tags"] = sorted(info["windows_tags"].items(), key=lambda x: x[1], reverse=True)
    info["mac_tags"] = sorted(info["mac_tags"].items(), key=lambda x: x[1], reverse=True)

    info["linux_tags"] = info["linux_tags"][:10]
    info["windows_tags"] = info["windows_tags"][:10]
    info["mac_tags"] = info["mac_tags"][:10]
    
    print(info)