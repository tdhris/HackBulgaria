import requests
import json
import os
from zipfile import ZipFile
import sqlite3

conn = sqlite3.connect("userpass.db")
cursor = conn.cursor()
cursor.execute("SELECT username, password FROM user")
my_user_info = cursor.fetchone()
my_username = my_user_info[0]
my_pass = my_user_info[1]
conn.close()

username = input("username> ")
unparsed_user_info = requests.get("https://api.github.com/users/{0}".format(username), auth=(my_username, my_pass))
userinfo = json.JSONDecoder().decode(unparsed_user_info.content.decode('utf-8'))
repos_url = userinfo["repos_url"]

repos = requests.get(repos_url, auth=(my_username, my_pass))
repos_info = json.JSONDecoder().decode(repos.content.decode('utf-8'))

working_directory = os.getcwd()
for repo in repos_info:
    r = requests.get("https://github.com/{0}/{1}/archive/master.zip".format(username, repo["name"]), auth=(my_username, my_pass))
    with open("{0}.zip".format(repo["name"]), "wb") as zip_file:
        zip_file.write(r.content)
        zip_file.close()

    with ZipFile("{0}/{1}".format(working_directory, repo["name"] + ".zip"), "r") as zip_file:
        zip_file.extractall()
