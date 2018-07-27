import csv 

'''
Code to reading and writing to Csv file using Csv module in python
'''

def readCsv(filename):
    with open(filename,'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            print(line)
    

def writeCsv(filename):
    with open(filename,'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        with open('new_csv_file.csv','w') as newfile:
            csv_writer = csv.writer(newfile,delimiter='-')
            for  line in csv_reader:
                csv_writer.writerow(line)
                
def readcsvDict(filname):
    print("Using Csv dict Reader")
    with open('Test.csv') as file:
        csv_reader = csv.DictReader(file)
        for line in csv_reader:
            print(line['fname'])
                
                
def writeCsvDict(filename):
    print("Writing to Csv using dict reader")
    with open()
if __name__=="__main__":
    writeCsv('Test.csv')
    #readCsv('Test.csv')
    readcsvDict('Test.csv')
    

