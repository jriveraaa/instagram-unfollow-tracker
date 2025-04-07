import json
import csv

def read_json_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)

        usernames = []

        if file_name == 'followers_1.json':
            for user in data:
                try:
                    username = user['string_list_data'][0]['value']
                    usernames.append(username)
                except (KeyError, IndexError) as e:
                    print(f"Error al acceder a los datos de un usuario en {file_name}: {e}")
                    continue

        elif file_name == 'following.json':
            relationships_following = data.get('relationships_following', [])
            for user in relationships_following:
                try:
                    username = user['string_list_data'][0]['value']
                    usernames.append(username)
                except (KeyError, IndexError) as e:
                    print(f"Error al acceder a los datos de un usuario en {file_name}: {e}")
                    continue

    return usernames

followers = set(read_json_file('followers_1.json'))
following = set(read_json_file('following.json'))

non_followers = following - followers

with open('non_followers.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Usuario"]) 
    for user in sorted(non_followers):
        writer.writerow([user])

print("Lista exportada a 'non_followers.csv'")
