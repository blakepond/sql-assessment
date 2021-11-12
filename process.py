# declaring the varible log_file and opening the data file us-server-01.txt
log_file = open("um-server-01.txt")

# declaring a new function called sales_reports and setting log_file as the parameter
def sales_reports(log_file):
    # running a for in loop creating the iterater "line" and looping through log_file
    for line in log_file:
        # delete white space 
        line = line.rstrip()
        # declaring a new variable called "day" and setting it equal to first element 
        day = line[0:3]
        # conditional statement if day is "Tue" then print the line
        if day == "Mon":
            print(line)
        
        
# invokes the function with the variable log_file
sales_reports(log_file)
