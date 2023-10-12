# list of names
names = ['Jessa', 'Eric', 'Bob']

# open file in write mode
with open(r'C:\Users\hermava\projects\python\machineLearning\base\users.txt', 'w') as fp:
    for item in names:
        # write each item on a new line
        fp.write("%s\n" % item)
    print('Done')