import json

def read():
    data_dict = {}
    with open('users.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

        for user in data['users']:
            data_dict['nombre'] = user['nombre']
            data_dict['edad'] = user['edad']
            print(data_dict)


def run():
    read()


if __name__ == '__main__':
    run()
