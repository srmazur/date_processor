import csv
import logging


class CommonUtils:
    @staticmethod
    def initialize_logging(level=logging.INFO):
        logging.basicConfig(
            level=level, format="%(asctime)s - %(levelname)s - %(message)s"
        )

    @staticmethod
    def write_csv(file_path, data):
        """Write list of data to a file."""
        try:
            with open(file_path, "w", newline="") as csv_file:
                csvwriter = csv.writer(csv_file)
                csvwriter.writerows([[item] for item in data])
            logging.info(f"Data successfully written to {file_path}")
        except IOError as e:
            logging.error(f"File I/O error: {e}")

    @staticmethod
    def write_report(report_path, report_data):
        """Write report data to a file."""
        try:
            with open(report_path, "w") as report_file:
                for key, value in report_data.items():
                    if key == "valid_date_times":
                        report_file.write(f"{key}: {len(value)}")
                    else:
                        report_file.write(f"{key}: {value}\n")
            logging.info(f"Report written to {report_path}")
        except IOError as e:
            logging.error(f"File I/O error: {e}")

    @staticmethod
    def format_timezone(hour, minute):
        """Format the timezone offset."""
        return [f"Z", f"+{hour:02}:{minute:02}", f"-{hour:02}:{minute:02}"]


CommonUtils.initialize_logging()
