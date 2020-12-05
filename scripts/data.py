import csv

from student.models import Student


def run():
	fhand = open('student/student.csv','r')
	reader = csv.reader(fhand)

	Student.objects.all().delete()


	for row in reader:
		print(row)
		L, created = Student.objects.get_or_create(Fname=row[0], Lname=row[1], Age=row[2], Email=row[3],Enr=row[5],Uni=row[4])
		L.save()
		