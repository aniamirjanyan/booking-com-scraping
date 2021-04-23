import json

with open('C:/Users/aniam/PycharmProjects/WebScraping/output500_final.json', errors="ignore") as json_file:
    data = json.load(json_file)


def item_count_list_of_lists():
    len_ = len(data)
    a = 0
    for i in range(len_):
        a += len(data[i])
    return a


def item_count():
    return len(data)


def append_all():
    flat_list = [item for sublist in data for item in sublist]
    with open('C:/Users/aniam/PycharmProjects/WebScraping/output500_final.json', 'w') as file_out:
        json.dump(flat_list, file_out)
    return flat_list


