from json import load, dump
from time import sleep
from dgupdater import check_update

def neutralize_app_version() -> None:
    with open('dgupdaterconf.json', 'r') as f:
        data = load(f)

    data['version'] = ""

    with open('dgupdaterconf.json', 'w') as f:
        dump(data, f, indent = 4)


def main() -> None:

    neutralize_app_version()

    # check_update()
    check_update(parallel=True)

    while True:
        print("Simulating running application...")
        sleep(.2)


if __name__ == '__main__':
    main()

    