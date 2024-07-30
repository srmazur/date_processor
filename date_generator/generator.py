import argparse

from utils.constants import Constants
from .base_generator import DateGenerator


def main():
    """Main function to parse arguments and generate data."""

    parser = argparse.ArgumentParser(
        description="Generate random date-time data, including duplicates and invalid dates as .csv file."
    )
    parser.add_argument("output_file")
    parser.add_argument("size", choices=["S", "L"])
    parser.add_argument(
        "--duplicate-ratio", type=float, default=Constants.DUPLICATE_RATIO
    )

    args = parser.parse_args()
    generator = DateGenerator(args.output_file, args.size, args.duplicate_ratio)
    generator.generate_data()


if __name__ == "__main__":
    main()
