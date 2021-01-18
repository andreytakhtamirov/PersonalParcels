import json
import datetime


def main():
    with open("message_1.json") as json_file:
        data = json.load(json_file)
        # print(data)
        for p in data['participants']:
            print('participants: ' + p['name'])

        print('\n')

        for p in data['messages']:
            if 'content' in p and p['content'] != "":
                print('sender: ' + p['sender_name'])
                print('time: ' + datetime.datetime.fromtimestamp(p['timestamp_ms'] / 1000).strftime('%Y-%m-%d %H:%M'))
                print('content: ' + p['content'])
                print('\n')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
