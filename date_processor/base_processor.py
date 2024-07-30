import re
from utils.constants import Constants
from utils.common_utils import CommonUtils


class DateProcessor:
    def __init__(self, input_file_path, output_file_path):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path

    def date_is_valid(self, date_time) -> bool:
        """Check if a date string matches the given format."""

        valid_pattern = re.compile(Constants.DATE_PATTERN)
        return valid_pattern.match(date_time) is not None

    def write_valid_dates(self, valid_dates, report):
        """Write valid dates and the report files."""

        CommonUtils.write_csv(self.output_file_path, valid_dates)
        report_csv_path = self.output_file_path.replace(".csv", "_report.csv")
        CommonUtils.write_report(report_csv_path, report)

    def process_lines(self, lines, seen_date_times) -> dict:
        """Process lines to find unique, valid date-times."""

        total_records = 0
        duplicates = 0
        invalid_records = 0
        valid_date_times = set()

        for line in lines:
            total_records += 1
            date_time = line.strip()
            if not self.date_is_valid(date_time):
                invalid_records += 1
                continue
            if date_time in seen_date_times:
                duplicates += 1
            else:
                valid_date_times.add(date_time)
                seen_date_times.add(date_time)

        return {
            "total_records": total_records,
            "duplicates": duplicates,
            "invalid_records": invalid_records,
            "valid_date_times": valid_date_times,
        }
