import random
from datetime import datetime, timedelta

# Generate a random date and time
start_date = datetime(2020, 1, 1)
end_date = datetime(2030, 12, 31)

time_between = end_date - start_date
random_days = random.randint(0, time_between.days)
random_seconds = random.randint(0, 86399)

random_datetime = start_date + \
    timedelta(days=random_days, seconds=random_seconds)

print("Random Date and Time:", random_datetime)
