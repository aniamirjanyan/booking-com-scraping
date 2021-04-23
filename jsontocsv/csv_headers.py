import csv
import json

df = open('dfile.csv', 'w')
csv_writer = csv.writer(df)

header = ['name', 'score', 'price', 'link', 'Country', 'City/Village', 'Type', 'Popularity', 'Season', 'Distance_from_search',
          'Rating', 'Free WiFi/Internet', 'Included Breakfast', 'Room service',
          'Non-smoking rooms', 'Room area', 'Air conditioning', 'TV', 'bathroom',
          'Soundproof', 'Minibar', 'Free toiletries', 'Towels', 'Socket near the bed', 'Heating', 'Hairdryer/Fan',
          'Electric kettle', 'Refrigerator', 'Pets/ Pet friendly', 'Kitchen', 'Oven', 'Dining area', 'Parking',
          'English spoken', 'Languages spoken', 'Desk', 'Mosquito net', 'Free cancellation',
          'Walking tours', 'massage', 'Airport Shuttle', 'Balcony', 'Washing machine']

csv_writer.writerow(header)




