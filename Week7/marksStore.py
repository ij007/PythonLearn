global TEST_CASE

TEST_CASE = str(input())

noStudents = int(input())

subs = str(input()).split(',')

students = {}

for i in range (noStudents):
    
    studDetails = input().split(',')
    
    studId = int(studDetails[0])
    
    students[studId] = {}
    
    
    for j in range(1,len(studDetails)):
        
       students[studId][subs[j]] = int(studDetails[j])

print(students)

'''

TEST CASE 1
2
id,sub1,sub2,sub3
1,85,65,90
2,100,56,34

TEST CASE 2
5
id,maths,physics,chemistry,biology,compsci
1,10,20,30,40,50
2,60,70,80,90,100
3,100,98,38,49,29
4,100,100,100,100,100
5,78,39,98,29,98

'''