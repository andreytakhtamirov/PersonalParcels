import json


def main():
    with open("message_1.json") as json_file:
        data = json.load(json_file)
        print(data)
        for p in data['participants']:
            print('participants: ' + p['name'])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
