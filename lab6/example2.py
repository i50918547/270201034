grades = list()
av_grades = list()

studentCount = int(input("How many students will enter the grades? "))
for i in range(studentCount):
	m_1 = int(input("midterm1: "))
	m_2 = int(input("midterm2: "))
	f = int(input("final: "))

	grades.append([m_1,m_2,f])
	av_grades.append(m_1*0.3+m_2*0.3+f*0.4)

