from datetime import datetime
def get_difference_between_dates(date1, date2):
    date_format = "%Y.%m.%d"
    date1_obj = datetime.strptime(date1, date_format)
    date2_obj = datetime.strptime(date2, date_format)
    return (date2_obj - date1_obj).days
print("\nTask 2.9")
date1 = "2023.10.23"
date2 = "2023.10.24"
print(get_difference_between_dates(date1, date2))