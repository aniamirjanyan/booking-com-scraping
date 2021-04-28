import json
import os

africa = ['Egypt', 'Morocco', 'South Africa', 'Tunisia',
          'Algeria', 'Zimbabwe', 'Mozambique', 'Ivory Coast', 'Kenya', 'Botswana']

americas = ['United States', 'Mexico', 'Canada', 'Argentina', 'Dominican Republic',
            'Brazil', 'Chile', 'Peru', 'Cuba', 'Colombia']

asia_pacific = ['China', 'Thailand', 'Japan', 'Malaysia', 'Hong Kong', 'Vietnam',
                'India', 'South Korea', 'Indonesia']

europe = ['France', 'Spain', 'Italy', 'Turkey', 'Germany', 'United Kingdom',
          'Austria', 'Greece', 'Portugal', 'Russia']

middle_east = ['Saudi Arabia', 'United Arab Emirates', 'Iran', 'Israel', 'Jordan',
               'Bahrain', 'Oman', 'Qatar', 'Lebanon']

head = []
for country in middle_east:  # Egypt
    for file in os.listdir(f"C:/Users/aniam/PycharmProjects/WebScraping/Final_Data/middle_east/"):  # Egypt_summer.json
        if file.startswith(country):  # EGYPT_summer.json
            with open(f"C:/Users/aniam/PycharmProjects/WebScraping/Final_JSONs/middle_east/{country}.json",
                      "w", encoding="utf-8") as outfile:

                with open(f"C:/Users/aniam/PycharmProjects/WebScraping/Final_Data/middle_east/{file}",
                          'r', encoding="utf-8") as infile:
                    file_data = json.load(infile)
                    head += file_data
                json.dump(head, outfile)
                outfile.close()
