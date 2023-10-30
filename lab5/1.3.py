def get_date_in_format(date):
    date_parts = date.split('.')
    return f"{date_parts[2]}.{date_parts[1]}.{date_parts[0]}"
print("\nTask 1.3")
date = "2023.10.23"
print(get_date_in_format(date))
