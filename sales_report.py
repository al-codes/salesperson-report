"""Generate sales report showing total melons each salesperson sold."""



salespeople = []
melons_sold = []

#Opens file, strips line of white space and splits up list into a list 
#called entries. Loops over file lines.
f = open('sales-report.txt') #could have a better variable name like file
for line in f:
    line = line.rstrip()
    entries = line.split('|')
    #accesses salesperson name and number of melons sold
    salesperson = entries[0] #salesperson 
    melons = int(entries[2]) #labels second group as melons

    #if salesperson is already in salespeople, add count of melons to 
    #melons sold
    if salesperson in salespeople:
        #find position of salesperson
        position = salespeople.index(salesperson)
        #use to position index melos sold
        melons_sold[position] += melons
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

#loop over indices of salespeople and use to index melons sold
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')

#How code should be cleaned up-
#create a function to open the file -- argument filename
#if else statements to add to list of melons if more found
#else list = same as melons sold
#make a funciton to print sales report with sales person and melons sold
#argument melons sold by the salesperson

#advantages of breaking into two functions -- can use different files, can 
#print individual names
