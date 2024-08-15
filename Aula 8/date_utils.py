import datetime as dt

def get_current_date():
    return dt.datetime.now()

def get_date_string(date):
    return date.strftime("%d/%m/%Y")

if __name__ == "__main__":
    print(get_current_date())
    print(get_date_string(get_current_date()))
