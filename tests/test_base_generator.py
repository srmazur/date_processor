import os
import pytest
from utils.constants import Constants
from date_generator.base_generator import DateGenerator

GENERATOR = DateGenerator("output.csv", "S", 0.3)


def test_generate_random_date_string():
    random_date = GENERATOR.generate_random_date_string()
    assert isinstance(random_date, str)

    date_format_found = False
    for fmt in Constants.DATE_FORMATS:
        try:
            formatted_date = random_date.format(fmt)
            date_format_found = True
            break
        except ValueError:
            continue
    assert date_format_found


def test_generate_data():
    output_file = "output.csv"

    GENERATOR.generate_data()

    assert os.path.exists(output_file)

    with open(output_file, "r") as file:
        content = file.read().strip()
        assert content != ""

    os.remove(output_file)


if __name__ == "__main__":
    pytest.main()
