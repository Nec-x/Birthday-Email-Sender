from send_emails import sender
from excell import sheet_values
from datetime import datetime


def send_bday_emails():
    """
    Gets information from primary Google sheet and sends a birthday email if a customer's birthdate is the current date.
    List of lists in form of [Name,Email,BdayDate].
    """

    sheet_vals = sheet_values()
    sheet_vals.pop(0)

    for customer in sheet_vals:
        cus = customer[2].split('-')
        date = datetime.now()

        if date.month == int(cus[0]) and date.day == int(cus[1]):
            sender(customer[0],customer[1])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    send_bday_emails()

