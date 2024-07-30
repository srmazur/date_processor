import pytest
from date_processor.small_file_processor import SmallFileProcessor


def test_process(mocker):
    processor = SmallFileProcessor("input.csv", "output.csv")

    mocker.patch.object(
        processor,
        "process_lines",
        return_value={
            "total_records": 100,
            "duplicates": 20,
            "invalid_records": 79,
            "valid_date_times": {"2025-01-23T12:34:56+01:00"},
        },
    )

    mocker.patch.object(processor, "write_valid_dates")

    mocker.patch(
        "builtins.open", mocker.mock_open(read_data="2025-01-23T12:34:56+01:00\n")
    )

    processor.process()

    processor.process_lines.assert_called_once()

    processor.write_valid_dates.assert_called_once()


if __name__ == "__main__":
    pytest.main()
