import json
import random
import os

seasons = {"spring": ('2021-05-09', '2021-05-10'),
           "summer": ('2021-07-14', '2021-07-15'),
           "fall": ('2021-10-14', '2021-10-15'),
           "winter": ('2022-01-14', '2022-01-15')}

facilities = ['Free WiFi', 'Restaurant', 'Room service', 'Bar',
              '24-hour front desk', 'Non-smoking rooms', 'Pets allowed',
              'Tea/coffee maker in all rooms']

services = ['Air conditioning', 'Flat-screen TV', 'Bathroom', 'Towels', 'Socket near the bed', 'Soundproofing',
            'Free toiletries', 'Minibar', 'Heating', 'Hairdryer', 'Electric kettle', 'Refrigerator',
            'Kitchen', 'Oven', 'Dining area', 'English', 'Mosquito net',
            'Walking tours', 'Massage', 'Balcony', 'Washing machine']

breakfast = ["Fabulous breakfast", "Good breakfast", "Breakfast", "Very good breakfast",
             "Exceptional breakfast", "Superb breakfast"]

africa = ['Egypt', 'Morocco', 'South Africa', 'Tunisia',
          'Algeria', 'Zimbabwe', 'Mozambique', 'Ivory Coast', 'Kenya', 'Botswana']

americas = ['United States', 'Mexico', 'Canada', 'Argentina', 'Dominican Republic',
            'Brazil', 'Chile', 'Peru', 'Cuba', 'Colombia']

asia_pacific = ['China', 'Thailand', 'Japan', 'Malaysia', 'Hong Kong', 'Macau', 'Vietnam',
                'India', 'South Korea', 'Indonesia']

europe = ['France', 'Spain', 'Italy', 'Turkey', 'Germany', 'United Kingdom',
          'Austria', 'Greece', 'Portugal', 'Russia']

middle_east = ['Saudi Arabia', 'United Arab Emirates', 'Iran', 'Israel', 'Jordan',
               'Bahrain', 'Oman', 'Qatar', 'Lebanon']




def flatten_list(list_):
    flat_list = []
    for item in list_:
        if isinstance(item, list):
            for i_ in item:
                flat_list.append(i_)
        else:
            flat_list.append(item)
    return flat_list


def get_index_data():
    with open(f'C:/Users/aniam/PycharmProjects/WebScraping/country_index.json', 'r', encoding="utf-8") as jf:
        return json.load(jf)


def json_new_format(file_name, continent, data_num):
    final_list = []
    with open(f'C:/Users/aniam/PycharmProjects/WebScraping/Data/{continent}/{file_name}', 'r', encoding="utf-8") as jf:
        data = json.load(jf)

    data = data[data_num]

    for ap_dict in data:
        new_dict = {}
        for key in ap_dict:

            if key == "important_facilities":
                fac_curr = list(ap_dict[key])
                for i in range(len(facilities)):
                    # -----------------------------------------
                    if facilities[i] in fac_curr:
                        new_dict.update({facilities[i]: 1})
                    else:
                        new_dict.update({facilities[i]: 0})
                    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                if "Airport shuttle" in fac_curr or "Airport shuttle (free)" in fac_curr:
                    new_dict.update({"Airport Shuttle": 1})
                else:
                    new_dict.update({"Airport Shuttle": 0})
                    # -----------------------------------------
                if '1 swimming pool' in fac_curr or '2 swimming pools' in fac_curr:
                    new_dict.update({"Swimming Pool": 1})
                else:
                    new_dict.update({"Swimming Pool": 0})
                    # -----------------------------------------
                if 'Free parking' in fac_curr:
                    new_dict.update({"Parking": 1})
                else:
                    new_dict.update({"Parking": 0})
                    # -----------------------------------------
                if any(x in breakfast for x in fac_curr):
                    new_dict.update({"Breakfast": 1})
                else:
                    new_dict.update({"Breakfast": 0})
            elif key == "services_offered":
                ser_curr = list(ap_dict[key])
                service_list = []
                for service in ser_curr:
                    service_list.append(service["type"])
                    service_list.append(service["value"])
                final_services = flatten_list(service_list)
                for i in range(len(services)):
                    if services[i] in final_services:
                        new_dict.update({services[i]: 1})
                    else:
                        new_dict.update({services[i]: 0})
                # -----------------------------------------
                if ("Airport shuttle (additional charge)" or "Airport shuttle") in final_services:
                    new_dict.update({"Airport Shuttle": 1})
                # -----------------------------------------
                if ("Outdoor swimming pool" or "Indoor swimming pool") in final_services:
                    new_dict.update({"Swimming Pool": 1})
                # -----------------------------------------
                if 'Street parking' or 'Secured parking' or 'Parking garage' in final_services:
                    new_dict.update({"Parking": 1})
            else:
                new_dict.update({key: ap_dict[key]})
            if ap_dict["score"] == "":
                new_dict.update({"score": round(random.uniform(6.5, 8.5), 1)})
        # ----------------------------------- Adding the season columns
        for i in seasons.keys():
            if i in file_name:
                new_dict.update({i: 1})
            else:
                new_dict.update({i: 0})
        # ----------------------------------- Adding the INDEX columns
        index_data = get_index_data()
        country = file_name.split('_')[0]
        for i in range(len(index_data)):
            if str(index_data[i]["Country"]) == country:
                new_dict.update({"Cost of Living Index": index_data[i]["Cost of Living Index"]})
                new_dict.update({"Rent Index": index_data[i]["Rent Index"]})
        final_list.append(new_dict)

    return final_list


def load_into_season_file(file_name, continent):
    with open(f'C:/Users/aniam/PycharmProjects/WebScraping/Data/{continent}/{file_name}', 'r', encoding="utf-8") as jf:
        data = json.load(jf)
    f_list = []
    for i in range(len(data)):
        _list = json_new_format(file_name, continent, i)
        f_list.append(_list)
    with open(f'C:/Users/aniam/PycharmProjects/WebScraping/Final_Data/{continent}/{file_name}', 'w', encoding='utf-8') as f:
        json.dump(f_list, f, ensure_ascii=False, indent=4)
        f.close()


def load_load(folder):
    for file in os.listdir(f"C:/Users/aniam/PycharmProjects/WebScraping/Data/{folder}/"):
        load_into_season_file(file, folder)


# load_load("asia_pacific")
