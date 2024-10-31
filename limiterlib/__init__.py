import csv
from datetime import datetime
from .config import LOG_DIR, LIMIT


def __gen_filename(log_dir=LOG_DIR):
    now = datetime.now()
    date_str = now.strftime("%Y%m%d")
    filename = log_dir / f"{date_str}.csv"
    filename.touch(mode=0o777, exist_ok=True)
    return filename


def __gen_time_str():
    now = datetime.now()
    return now.strftime("%Y%m%d%H%M%S")


def is_limited(limit=LIMIT):
    filename = __gen_filename()
    with filename.open(mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        entry_count = len(rows)
    return entry_count >= limit


def record():
    filename = __gen_filename()
    time_str = __gen_time_str()
    with filename.open(mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([time_str])
