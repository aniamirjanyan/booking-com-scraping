import json


facilities = ['Family rooms', 'Free WiFi', 'Restaurant', 'Room service', 'Bar',
              '24-hour front desk', 'Non-smoking rooms', 'Pets allowed',
              'Tea/coffee maker in all rooms']

services = ['Air conditioning', 'Flat-screen TV', 'Bathroom', 'Towels', 'Socket near the bed', 'Soundproofing',
            'Free toiletries', 'Minibar', 'Heating', 'Hairdryer', 'Electric kettle', 'Refrigerator',
            'Kitchen', 'Oven', 'Dining area', 'English', 'Mosquito net',
            'Walking tours', 'Massage', 'Balcony', 'Washing machine']

breakfast = ["Fabulous breakfast", "Good breakfast", "Breakfast", "Very good breakfast",
             "Exceptional breakfast", "Superb breakfast"]

with open('C:/Users/aniam/PycharmProjects/WebScraping/Egypt_Summer2.json', 'r', encoding="utf-8") as jf:
    data = json.load(jf)

data = data[0]


def flatten_list(list_):
    flat_list = []
    for item in list_:
        if isinstance(item, list):
            for i_ in item:
                flat_list.append(i_)
        else:
            flat_list.append(item)
    return flat_list


final_list = []

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
    final_list.append(new_dict)


with open("EgyptSummer_test.json", 'w', encoding='utf-8') as f:
    json.dump(final_list, f, ensure_ascii=False, indent=4)
    f.close()
