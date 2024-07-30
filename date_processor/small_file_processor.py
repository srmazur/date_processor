from date_processor.base_processor import DateProcessor


class SmallFileProcessor(DateProcessor):
    def process(self):
        """Processing the input file at once to find unique, valid dates"""

        with open(self.input_file_path, "r") as file:
            lines = file.readlines()
            result = self.process_lines(lines, set())
        self.write_valid_dates(result["valid_date_times"], result)
