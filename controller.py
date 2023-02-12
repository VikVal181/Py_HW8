import data_base
import view

def start():
	while True:
		if data_base.set_class_name(view.select_class()):
			break
		else:
			view.print_class_error()
	
	view.show_subjects(data_base.get_subjects())
	
	while True:
		if data_base.set_subject(view.select_subject()):
			break
		else:
			view.print_subject_error()
	
	data_base.open_journal_subject()
	
	while True:
		journal = data_base.get_journal()
		view.show_list_of_students(journal)
		while True:
			student = view.choose_who_answer()
			if data_base.check_student(student):
				break
			else:
				view.print_student_error()
		if student == 'exit':
			break
		data_base.put_grade(student, view.what_grade())
	data_base.save()
	#match user_choice:
		#case 1:
		#case 2:
			#pass
		
