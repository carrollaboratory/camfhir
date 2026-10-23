from argparse import ArgumentParser

from helpers import Config


def main():
    parser = ArgumentParser("Update fixtures for dbt")

    args = parser.parse_args()
    config = Config.configuration()
    print("Hello world")


if __name__ == "__main__":
    main()
