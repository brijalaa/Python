tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
            ]
#print(tableData[0])
#print(len(tableData))

def printtable(data):
    colwidth = [0] * len(data) #which will create a list containing the same number of 0 values as the number of inner lists in tableData.
    max_length = [max(len(str) for str in data) for col in data]
    for word in data:
        print(data.ljust(max_length))


printtable(tableData)