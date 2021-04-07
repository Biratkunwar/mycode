#!/usr/bin/env python3

# we want to work with csv data
import csv

def main():
    # open our csv data
    with open("csv_users.txt", "r") as f:
        i = 0 # start a simple loop counter
        # loop across all of our csv data
        for row in csv.reader(f):
            i = i + 1 # simple counter (how many times through the loop)
            filename = f"admin.rc{i}"    # f-string -- fill in {} with var value
            
            # create the admin.rc{i} file
            with open(filename, "w") as rcfile:
                print("export OS_AUTH_URL=" + row[0], file=rcfile)
                print("export OS_IDENTITY_API_VERSION=3", file=rcfile)
                print("export OS_PROJECT_NAME=" + row[1], file=rcfile)
                print("export OS_PROJECT_DOMAIN_NAME=" + row[2], file=rcfile)
                print("export OS_USERNAME=" + row[3], file=rcfile)
                print("export OS_USER_DOMAIN_NAME=" + row[4], file=rcfile)
                print("export OS_PASSWORD=" + row[5], file=rcfile)

main()
