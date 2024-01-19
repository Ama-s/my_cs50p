from datetime import datetime

def get_formatted_date(user_input):
    try:
        # Try parsing the input as month-day-year format
        date_obj = datetime.strptime(user_input, "%m/%d/%Y")
        return date_obj.strftime("%Y-%m-%d")
    except ValueError:
        try:
            # Try parsing the input as a full date
            date_obj = datetime.strptime(user_input, "%B %d, %Y")
            return date_obj.strftime("%Y-%m-%d")
        except ValueError:
            # Invalid date format
            return None

def main():
    while True:
        user_input = input("Date: ").strip()
        formatted_date = get_formatted_date(user_input)

        if formatted_date is not None:
            print(f"{formatted_date}")
            break


main()
