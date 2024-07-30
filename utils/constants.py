class Constants:

    DATE_FORMATS = [
        "{month:02d}/{day:02d}/{year:04d}",
        "{month:02d}/{day:02d}/{year:04d} {hour:02d}:{minute:02d}:{second:02d}",
        "{day:02d}-{month:02d}-{year:04d} {hour:02d}:{minute:02d}",
        "{year:04d}.{month:02d}.{day:02d} {hour:02d}:{minute:02d}:{second:02d}",
        "{year:04d}-{month:02d}-{day:02d}T{hour:02d}:{minute:02d}:{second:02d}{time_zone}",
    ]

    SIZE_MAP = {"S": 100, "L": 100000}

    DUPLICATE_RATIO = 0.3

    HOUR_MAX = 23
    TIME_UNIT_MAX = 59
    DAY_MAX = 31
    MONTH_MAX = 12
    YEAR_MAX = 9999
    TIMEZONE_OFFSETS = ["Z"]

    # YYYY-MM-DDThh:mm:ssTZD
    DATE_PATTERN = r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(Z|[+-]\d{2}:\d{2})$"
