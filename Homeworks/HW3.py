#Create 5 students. Ask these students from the user.
#Each of these students should have a midterm grade, project grade and final grade.
#Each students will have a course passing grade.
#passingGrade = midterm*(0.3)+project*(0.3)+final*(0.4) passing grade should be determined like this.
#Create a dictionary that keeps these students' information.
#Calculate the students' grades and transfer them to the list with the help of indexing.
#Finally, set the student with the highest grade to be in the first index and the student with the lowest grade to be in the last index of the list.


#Question 1

#öğrencilerin ortalamalarını hesaplar
def grade():
    passingGrade = []
    
    for i in range(1,6):
        midterm = float(input(f'{i}. öğrencinin vize notu nedir:'))
        project = float(input(f'{i}. öğrencinin proje notu nedir:'))
        final = float(input(f'{i}. öğrencinin final notu nedir:'))
        
        passingGrade.append(midterm*(0.3) + project*(0.3) + final*(0.4))
        print("\n")
        
    return passingGrade


grades = {"1.öğrenci": 0,"2.öğrenci": 0,"3.öğrenci": 0,"4.öğrenci": 0,"5.öğrenci": 0,}
allGrade = []

test = grade()

#öğrenci ve ortalamalarından oluşan bir dictionary yapar
j = 0
for i in grades.keys():
    grades[i] = test[j]
    j += 1
    
print("\n",grades,"\n")
    
#öğrenci ortalamlarından oluşan bir liste yapar
for x in grades.values():
    allGrade.append(x)

allGrade.sort() #listeyi sıralar
allGrade.reverse() #listeyi ters çevirir

print(allGrade)
