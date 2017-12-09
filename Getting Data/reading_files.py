import re
import collections
import csv
from Tools.scripts.finddiv import process

if __name__ == '__main__':

    file_for_reading = open("file.txt", 'r')
    file_for_writing = open("file.txt", 'w')
    file_for_appending = open("file.txt", 'a')

    file_for_writing.close()

    # need whole text file
    starts_with_hash = 0
    with open("file.txt", 'r') as f:
        for line in f:
            if re.match("^#", line):   # use regex to see if it starts with '#'
                starts_with_hash += 1

    # to get an email address from a text file

    def get_domain(email_address):
        return email_address.lower().split("@")[-1]

    with open('email_addresses.txt', 'r') as f:
        domain_counts = collections.Counter(get_domain(line.strip())
                                            for line in f
                                            if '@' in line)

    # file without headers
    with open("file.txt", 'rb') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            date = row[0]
            symbol = row[1]
            closing_price = row[2]

        process(date, symbol, closing_price)

    # file with headers
    with open("file.txt", 'rb') as f:
        reader = csv.DictReader(f, delimiter=':')
        for row in reader:
            date = row["date"]
            symbol = row["symbol"]
            closing_price = float(row["closing_price"])

        process(date, symbol, closing_price)

    # writing in a file

    today_prices = {'AAPL': 90.91, 'MSFT': 41.68, 'FB': 64.5}
    with open("file.txt", 'rb') as f:
        writer = csv.writer(f, delimiter=",")
        for stock, prices in today_prices.items():
            writer.writerow([stock, prices])




