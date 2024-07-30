import random
import logging
from utils.constants import Constants
from utils.common_utils import CommonUtils


class DateGenerator:
    def __init__(self, output_file: str, size: str, duplicate_ratio: float):
        self.output_file = output_file
        self.size = size
        self.duplicate_ratio = duplicate_ratio

    def generate_random_date_string(self) -> str:
        """Generate a random date string in one of the specified formats."""

        random_hour = random.randint(0, Constants.HOUR_MAX)
        random_time_unit_max = random.randint(0, Constants.TIME_UNIT_MAX)
        date_values = {
            "year": random.randint(0, Constants.YEAR_MAX),
            "month": random.randint(1, Constants.MONTH_MAX),
            "day": random.randint(1, 31),
            "hour": random_hour,
            "minute": random_time_unit_max,
            "second": random_time_unit_max,
            "time_zone": random.choice(
                CommonUtils.format_timezone(random_hour, random_time_unit_max)
            ),
        }
        format_string = random.choice(Constants.DATE_FORMATS)
        return format_string.format(**date_values)

    def generate_data(self):
        """Generate dates and write it to a file."""

        try:
            number_of_records = Constants.SIZE_MAP[self.size]
            number_of_duplicates = int(number_of_records * self.duplicate_ratio)

            unique_dates = [
                self.generate_random_date_string()
                for _ in range(number_of_records - number_of_duplicates)
            ]

            duplicates = random.choices(unique_dates, k=number_of_duplicates)

            all_dates = unique_dates + duplicates
            random.shuffle(all_dates)

            CommonUtils.write_csv(self.output_file, all_dates)

        except KeyError as e:
            logging.error(f"Invalid size '{self.size}' provided: {e}")
