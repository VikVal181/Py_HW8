path = ''
subject = ''
journal = {}

def set_class_name(name: str):
	global path
	classes_list = ['1А','2А','3А','4А','5А','6А','7А','8А','9А','10А','11А']
	if name in classes_list:
		path = name + '.txt'
		return True
	else:
		return False
		
def open_journal():
	with open(path, 'r', encoding='UTF-8') as file:
		data = file.readlines()
	return data
	
def get_subjects():
	subject_list = []
	data = open_journal()
	for line in data:
		subject_list.append(line.split(';')[0])
	return subject_list

def set_subject(subject_title: str):
	global subject
	if subject_title in get_subjects():
		subject = subject_title
		return True
	else:
		return False

def open_journal_subject():
	global path
	global subject
	data = open_journal();
	for line in data:
		if line.split(';')[0] == subject:
			for students in line.split(';')[1].strip().split(', '):
				journal[students.split(':')[0]] = list(map(int, students.split(':')[1].split()))


def get_journal():
	global journal
	return journal
	
def put_grade(student: str, grade: int):
	grades = journal.get(student)
	grades.append(grade)
	journal[student] = grades
	
def check_student(student: str):
	global journal
	if student in journal or student == 'exit':
		return True
	else:
		return False
	
	
def save():
	global journal
	global subject
	global path
	new_file = []
	data = open_journal()
	for sub in data:
		if sub.split(';')[0] != subject:
			new_file.append(sub.strip())
	item = []
	for student, grade in journal.items():
		item.append(student + ':' + ' '.join(list(map(str, grade))))
	item = subject + ';' + ', '.join(item)
	new_file.append(item)
	with open(path, 'w', encoding='UTF-8') as data:
		data.write('\n'.join(new_file))
		
