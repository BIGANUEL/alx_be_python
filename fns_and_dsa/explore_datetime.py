from datetime import datetime,timedelta


def display_current_datetime():
    current_date = datetime.now()
    formatted_Date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_Date)

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: ")) 
    future_date = datetime.now() + timedelta(days=number_of_days)  
    formatted_future_date = future_date.strftime("%Y-%m-%d")  
    print("Future date:", formatted_future_date)

if __name__ == "__main__":
    display_current_datetime()  
    calculate_future_date()  