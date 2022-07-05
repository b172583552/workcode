import os

requiredlist=[]
outstandinglist = []
code = "FM"
matchstr = "Outstanding: "
outstanding = 0
currency = {"HKD": 1.0300, "RMB": 1.2537, "USD": 8.0113, "GBP": 11.0516}

with open('29-10-2021.txt') as fo:
    for rec in fo:
        if rec[0:2] == code:
            requiredlist.append(outstanding)
            outstanding = 0
            output = ""
            for i in rec:
                output += i
                if i == " ":
                    requiredlist.append(output)
                    break
        for k in currency:
            if k in rec:
                curr_currency = currency[k]
        if matchstr in rec:
            temp = rec[13:]
            temp = temp.replace(",", "")
            temp = temp.strip("\n")
            outstanding += (float(temp) * curr_currency)
    requiredlist.append(outstanding)
del requiredlist[0]
# Open a file
acc = open("acc.txt", "w")
outstandingfile = open("outstanding.txt", "w")
for i in range(len(requiredlist)):
    if i%2 == 1:
        print(requiredlist[i])
        outstandingfile.write(str(requiredlist[i])+"\n")
    else:
        print(requiredlist[i])
        acc.write(str(requiredlist[i])+"\n")
# Close opend file













