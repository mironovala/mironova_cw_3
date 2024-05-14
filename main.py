from utils.utils import get_executed
from utils.utils import operation_output


def main():
    items = get_executed()

    for i in range(5):
        print(operation_output(items[i]))
        print()


if __name__ == "__main__":
    main()
