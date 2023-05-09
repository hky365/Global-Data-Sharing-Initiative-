#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import datetime

data = pd.read_csv("<file_path_origin>")

def apply_random_offset(date_str):
    if not isinstance(date_str, str):
        return date_str
    
    # Parse the date string
    date = datetime.datetime.strptime(date_str, "%d/%m/%Y")
    
    # Generate a random offset (e.g., between -15 and 15 days)
    offset = random.randint(-15, 15)
    offset = datetime.timedelta(days=offset)
    
    # Apply the offset to the date
    new_date = date + offset
    
    # Return the new date as a string
    return new_date.strftime("%d/%m/%Y")

# Apply the random offset to the stop_or_end_date_combined column
data['stop_or_end_date_combined'] = data['stop_or_end_date_combined'].apply(apply_random_offset)


# Save the modified dataset
data.to_csv("<file_path_destination>", index=False)

