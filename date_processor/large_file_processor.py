from date_processor.base_processor import DateProcessor


class LargeFileProcessor(DateProcessor):
    def read_file_in_parts(self, part_size=1024 * 1024):
        with open(self.input_file_path, "r") as file:
            while True:
                lines = file.readlines(part_size)
                if not lines:
                    break
                yield lines

    def process(self):
        """Processing the input file in parts to find unique, valid dates"""

        total_records = 0
        duplicates = 0
        invalid_records = 0
        valid_date_times = set()
        seen_date_times = set()

        for part in self.read_file_in_parts():
            result = self.process_lines(part, seen_date_times)
            total_records += result["total_records"]
            duplicates += result["duplicates"]
            invalid_records += result["invalid_records"]
            valid_date_times.update(result["valid_date_times"])
            seen_date_times.update(result["valid_date_times"])

        report = {
            "total_records": total_records,
            "duplicates": duplicates,
            "invalid_records": invalid_records,
            "valid_date_times": valid_date_times,
        }

        self.write_valid_dates(valid_date_times, report)
