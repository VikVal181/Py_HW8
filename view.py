def select_class():
	return input('Введите название класса: ').upper()

def select_subject():
	return input('Введите название предмета: ').lower()
	
def show_list_of_students(journal: dict):
	for i, student in enumerate(journal, 1):
		print(f'{i}. {student:20} {journal.get(student)}')

def what_grade():
	grade = 0
	flag = False
	while grade < 1 or grade > 5:
		if flag:
			print('Поставленна не существующая оценка! Поставте корректную оценку')
		grade = int(input('Поставте оценку: '))
		flag = True
	return grade
		
def choose_who_answer():
	return input('Введите имя ученика: ')
	
def print_student_error():
	print('Такого ученика нет в этом классе')
	
def print_class_error():
	print('Такого класса нет')

def print_subject_error():
	print('Такого предмета в этом класее не изучается')
	
def show_subjects (subjects:list):
	print("\nСписок предметов:")
	print('\n'.join(subjects))
