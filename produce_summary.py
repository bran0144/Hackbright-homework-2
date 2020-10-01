def melon_count(day, file_path):
    """Function creates to list the type of melons, count them, and total amount"""
    print("Day", day)
    log = open(file_path)

    for line in log:   #Creates a for loop to iterate through the file
        line = line.rstrip()    #Strips the right side of white space
        words = line.split('|') #Splits line into separate strings
        melon = words[0]    #Selects type of melon
        count = words[1]    #Selects count of melon
        amount = words[2]   #Selects total amount of melons

    print("Delivered {} {}s for total of ${}".format(   #print statement to print off amounts
        count, melon, amount))

melon_count(1, "um-deliveries-20140519.txt")


melon_count(2, "um-deliveries-20140520.txt")


melon_count(3, "um-deliveries-20140521.txt")
