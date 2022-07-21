import os

requiredlist = []
outstandinglist = []
code = input("code: ")
matchstr = "Outstanding:"
outstanding = 0
HKD,RMB,USD,GBP = [float(i) for i in input("HKD,RMB,USD,GBP ").split()]
currency = {"HKD": HKD, "RMB": RMB, "USD": USD, "GBP": GBP}
textfile = input("textfile: ")
with open(textfile) as fo:
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
            temp = ""
            for char in reversed(rec[0:rec.find(matchstr)]):
                temp += char
                if char == " ":
                    break
            temp = temp[::-1]
            temp = temp.replace(",", "")
            temp = temp.strip("\n")
            temp = temp.strip()
            outstanding += (float(temp) * curr_currency)
    requiredlist.append(outstanding)
del requiredlist[0]




# Open a file
acc = open("account.txt", "w")
outstandingfile = open("outstanding.txt", "w")
for i in range(len(requiredlist)):
    if i % 2 == 1:
        print(requiredlist[i])
        outstandingfile.write(str(requiredlist[i])+"\n")
    else:
        print(requiredlist[i])
        acc.write(str(requiredlist[i])+"\n")
# Close opend file








