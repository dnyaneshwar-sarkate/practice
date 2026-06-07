##Python programme to demonstarte working of positional and key-word arguments

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'CompSci']
info = {'name': 'John', 'age': 25}

student_info(*courses, **info)