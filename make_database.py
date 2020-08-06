import sqlite3
import json

conn = sqlite3.connect('mastodon_data.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Metadata')

cur.execute('''
CREATE TABLE Metadata (id TEXT UNIQUE PRIMARY KEY NOT NULL, name TEXT UNIQUE, short_description TEXT, full_description TEXT, topic TEXT, languages TEXT, prohibited_content TEXT, categories TEXT)''')

line = None

with open("clean.txt", "r") as file1:
    data = json.dumps(json.load(file1))
    print(data)
conn.commit()