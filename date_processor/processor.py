import os
import logging
import argparse
from date_processor.small_file_processor import SmallFileProcessor
from date_processor.large_file_processor import LargeFileProcessor


def main():
    """Main function to process the file and generate a valid dates file with a report."""

    parser = argparse.ArgumentParser(
        description="Find unique date-time values in valid format from a file."
    )
    parser.add_argument("input_file")
    parser.add_argument("output_file")

    args = parser.parse_args()
    input_file_path = args.input_file
    output_file_path = args.output_file

    try:
        file_size = os.path.getsize(input_file_path)
    except OSError as e:
        logging.error(f"Error getting size of input file: {e}")
        return

    if file_size < 1024 * 1024:  # Less than 1 MB
        logging.info(f"File size is: '{file_size}' bytes, processing file in once.")
        processor = SmallFileProcessor(input_file_path, output_file_path)
    else:
        logging.info(f"File size is: '{file_size}' bytes, processing file in parts.")
        processor = LargeFileProcessor(input_file_path, output_file_path)

    try:
        processor.process()
    except Exception as e:
        logging.error(f"Error processing file: {e}")


if __name__ == "__main__":
    main()
