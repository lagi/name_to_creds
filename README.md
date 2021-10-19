# Name to credentials

Use this script to modify a list of names into credentials of your desired format e.g. John Doe -> DOMAIN\johndoe, john.doe, doejohn, johndoe001 etc.

Useful for username enumeration purposes.


usage: name_to_creds.py [-h] [-firstname FIRSTNAME] [-lastname LASTNAME] [-delimiter DELIMITER] [-reverse]
                        [-start START] [-end END]
                        filename

positional arguments:
  filename              Name of the source file

optional arguments:
  -h, --help            show this help message and exit
  -firstname FIRSTNAME  Desired lenght of first name
  -lastname LASTNAME    Desired lenght of last name
  -delimiter DELIMITER  Delimiter between first and last name
  -reverse              Reverse first and last names
  -start START          Start the username with a specified string
  -end END              End the username with a specified string
