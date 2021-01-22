import datetime
import json


def main():
    with open("message_23.json") as json_file:
        data = json.load(json_file)

        # print(data)
        for p in data['participants']:
            print('participants: ' + p['name'])

        print('')

        for p in data['messages']:
            if 'content' in p and p['content'] != "":
                print('sender: ' + p['sender_name'])
                print('time: ' + convert_time(p['timestamp_ms']))
                print('content: ' + p['content'])
                print('')

            elif 'photos' in p:
                for p in p['photos']:
                    print('url: ' + p['uri'])
                    # print('creation timestamp: ' + convert_time(p['creation_timestamp']))
                    print('')


def convert_time(ms_since_1970):
    return datetime.datetime.fromtimestamp(ms_since_1970 / 1000).strftime('%Y-%m-%d %H:%M')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
