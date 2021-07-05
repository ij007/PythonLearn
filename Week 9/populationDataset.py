def solution():
   
   file = open('WorldPopulation.csv','r')
   
   year = str(input())        # year input Q.1
   population = str(input())  # population exceed Q.2
   maxheader = str(input())  # max of header file in dataset Q.3

   yearFlag = 0
   populationFlag = 0
   maxheaderval = 0.0

   dataset = file.readlines()

   line = dataset[0].split(',')
   line[-1] = line[-1].strip()

   index = line.index(maxheader)

   for records in dataset[1:]:

     records = records.split(',')

     if(yearFlag == 0):

       if(records[0] == year):

         yearPop = int(records[1].strip())
         yearFlag = 1


     if(int(records[1]) > int(population)):

        maxPop = int(records[0].strip())

     if(float(records[index].strip()) > float(maxheaderval)):

       maxheaderval = float(records[index].strip())

   file.close()

   print(yearPop)
   
   if(yearFlag!=0):    
       print(maxPop)
   else:
       line = dataset[-1].split(',')
       print(line[0])
    
   print(maxheaderval)
