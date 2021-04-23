import json
import datetime
from booking_scraper.booking_scraper import bkscraper

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

seasons = [('2021-04-14', '2021-04-15'), ('2021-07-14', '2021-07-15'),
           ('2021-10-14', '2021-10-15'), ('2022-01-14', '2022-01-15')]

result = bkscraper.get_result(country='France', limit=1, people=2, detail=True,
                              datein="2021-07-12", dateout="2021-07-13")

with open("France_Summer2.json", 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)
    f.close()


# def get_data(country_list, season):
#     for country in country_list:
#         raw = bkscraper.get_result(country=country, limit=12, people=2, detail=True,
#                                    datein=season[0], dateout=season[1])
#         with open(f"{country}_{season}.json", 'w', encoding='utf-8') as fl:
#             json.dump(result, fl, ensure_ascii=False, indent=4)
#             fl.close()

