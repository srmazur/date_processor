# Date Processor

## Overview
Date Processor is a Python project designed to generate and process date-time data. The project consists of two main components:

1. **Date Generator**: Generates random date-time data in various formats.
2. **Date Processor**: Processes the generated date-time data to identify valid, duplicate, and invalid records.

## Features

- **Run with Python**: Generate and process dates using Python.
  
- **Run with Docker**: Use Docker to generate and process dates, ensuring a consistent environment across different systems.

- **CI/CD with GitHub Actions**: Automated testing and deployment workflow is set using GitHub Actions.

## Requirements

- Python 3.12
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/DateProcessor.git
    cd DateProcessor
    ```

2. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Running with Python

#### Date Generator

Generate random date-time data and save it to a CSV file.

```sh
python -m date_generator.generator <output_file> <file_size>
```
- <output_file>: Path to the output CSV file.
- <file_size>: Size of the dataset. Options are S (small) or L (large).

Example:
```sh
python -m date_generator.generator generated_data.csv S
```

#### Date Processor

Process the generated dates and save the results to new CSV files.

```sh
python -m date_processor.processor <input_file> <output_file>
```
- <input_file>: Path to the input CSV file with generated dates.
- <output_file>: Path to the output CSV file to save processed data.

Example:
```sh
python -m date_processor.processor generated_data.csv processed_data.csv
```


### Running with Docker

#### Date Generator

Generate random dates data using Docker Compose.

```sh
docker-compose run date_generator <output_file> <file_size>
```
- <output_file>: Path to the output CSV file.
- <file_size>: Size of the dataset. Options are S (small) or L (large).

Example:
```sh
docker-compose run date_generator generated_data.csv S
```

#### Date Processor

Process the generated dates using Docker Compose.

```sh
docker-compose run date_processor <input_file> <output_file>
```
- <input_file>: Path to the input CSV file with generated dates.
- <output_file>: Path to the output CSV file to save processed data.

Example:
```sh
docker-compose run date_processor generated_data.csv processed_data.csv
```

Cleanup:
```sh
docker-compose down
```