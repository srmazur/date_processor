import pytest
from date_processor.base_processor import DateProcessor

VALID_DATE = "2043-09-21T11:30:00-04:00"
INVALID_DATE = "01/24/2030 12:44:70"
PROCESSOR = DateProcessor("input.cvs", "output.cvs")


def test_date_is_valid():
    assert PROCESSOR.date_is_valid(VALID_DATE) is True
    assert PROCESSOR.date_is_valid(INVALID_DATE) is False


def test_write_unique_valid_date_times(mocker):
    report = {
        "total_records": 1,
        "duplicates": 0,
        "invalid_records": 0,
        "valid_unique_records": 1,
    }
    mock_open = mocker.mock_open()
    mocker.patch("builtins.open", mock_open)
    PROCESSOR.write_valid_dates(VALID_DATE, report)
    mock_open.assert_called()


if __name__ == "__main__":
    pytest.main()
