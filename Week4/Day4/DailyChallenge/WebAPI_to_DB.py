# Daily challenge : Web API to DB
#     Using this API, create the functionality which will write 10 random countries to your database.
#
#     These are the attributes which you should populate your tables with: name, capital, flag, subregion, population.

import requests, random, sqlite3

response = requests.get("https://restcountries.com/v3.1/all")
countries = response.json()

random_countries = random.sample(countries, 10)

# Create database
with sqlite3.connect('countries.db') as connection:
    cursor = connection.cursor()

create_table_query = '''
        CREATE TABLE IF NOT EXISTS countries (
            name TEXT,
            capital TEXT,
            flag TEXT,
            subregion TEXT,
            population INTEGER
        )
    '''

# Create Table in Database
cursor.execute(create_table_query)

# Insert values to the table
for country in random_countries:
    name = country.get('name', {}).get('common')
    capital = country.get('capital', ['N/A'])[0]
    flag = country.get('flag', 'N/A')
    subregion = country.get('subregion', 'N/A')
    population = country.get('population', 0)

    # # Encode the flag value using UTF-8 encoding
    # flag = flag.encode('utf-8')

    insert_query = '''
            INSERT INTO countries (name, capital, flag, subregion, population)
            VALUES (?, ?, ?, ?, ?)
        '''
    cursor.execute(insert_query, (name, capital, flag, subregion, population))

connection.commit()
connection.close()
