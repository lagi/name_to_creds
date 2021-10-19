import sys
import argparse


# command line arguments

parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str, help='Name of the source file')
parser.add_argument('-firstname', type=int, help='Desired length of first name')
parser.add_argument('-lastname', type=int, help='Desired length of last name')
parser.add_argument('-delimiter', type=str, help='Delimiter between first and last name')
parser.add_argument('-reverse', action='store_true', help='Reverse first and last names')
parser.add_argument('-start', type=str, default="", help='Start the username with a specified string')
parser.add_argument('-end', type=str, default="", help='End the username with a specified string')

args = parser.parse_args()


# save arguments

first = args.firstname
last = args.lastname
delimiter = args.delimiter
reverse = args.reverse
filename = args.filename
start = args.start
end = args.end



# read all lines
file = open(filename,'r')
lines = file.readlines()

# create output file
if "." in filename:
   dot = filename.index(".")
   filename = filename[:dot]

output = filename + "_firstname_"+str(first)+"-lastname_"+str(last)+"-delimiter_"+delimiter+"-reverse_"+str(reverse)+"-start_"+start+"-end_"+end
newfile = open(output+'.txt','w')

# iterate through every line

for line in lines:
   space = line.index(" ")
   line = line.strip()
   
   # first name
   if not first:
      firstname = line[:space]
   else:
      firstname = line[:first]

   # last name
   if not last:
      lastname = line[space+1:]
   else:
      lastname = line[space+1:space+1+last]
   
   # assemble username
   username = ""
   
   if reverse:
      username = lastname + delimiter + firstname
   else:
      username = firstname + delimiter + lastname
   
   # formatting

   username = username.lower()
   username = username.replace('ä','a')
   username = username.replace('ö','o')
   
   # add start and end
   
   username = start + username
   username += end

   username += "\n"
   
   newfile.write(username)


newfile.close
file.close
print("Output printed to " + output + ".txt")