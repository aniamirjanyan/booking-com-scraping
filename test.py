import json
import datetime
from booking_scraper.booking_scraper import bkscraper
from jsontocsv.json_change_format import seasons, africa, asia_pacific, middle_east, europe, americas


# result = bkscraper.get_result(country='France', limit=1, people=2, detail=True,
#                               datein="2021-07-12", dateout="2021-07-13")
#
# with open("France_Summer2.json", 'w', encoding='utf-8') as f:
#     json.dump(result, f, ensure_ascii=False, indent=4)
#     f.close()


def get_data(country_list, season):
    date_ = seasons[season]
    for country in country_list:
        raw = bkscraper.get_result(country=country, limit=8, people=2, detail=True,
                                   datein=date_[0], dateout=date_[1])
        with open(f"Data/asia_pacific/{country}_{season}.json", 'w', encoding='utf-8') as fl:
            json.dump(raw, fl, ensure_ascii=False, indent=4)
            fl.close()


# get_data(middle_east, "spring")
