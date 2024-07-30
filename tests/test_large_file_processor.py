import pytest
from date_processor.large_file_processor import LargeFileProcessor


def test_process(mocker):
    processor = LargeFileProcessor("input.csv", "output.csv")

    mocker.patch.object(
        processor, "read_file_in_parts", return_value=[["2023-07-28T12:34:56Z\n"]]
    )

    mocker.patch.object(processor, "write_valid_dates")

    processor.process()

    processor.read_file_in_parts.assert_called_once()

    processor.write_valid_dates.assert_called_once()


if __name__ == "__main__":
    pytest.main()
