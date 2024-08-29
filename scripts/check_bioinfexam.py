
import sys, os
import importlib

sys.path.append('.')

_, facit_file, student_file, output_file = sys.argv

os.chdir(os.path.split(student_file)[0])

facit_basename = os.path.splitext(os.path.split(facit_file)[1])[0]
facit = __import__(facit_basename)

answer_basename = os.path.splitext(os.path.split(student_file)[1])[0]
answer = __import__(answer_basename)

#student_name = answer_basename.split('_')[0]

with open(output_file, 'w') as f:
	for statement in [x for x in dir(facit) if x.startswith('emne')]:
		# print(student_name, statement, getattr(answer, statement), getattr(facit, statement), sep=',', file=f)
		print(statement, getattr(answer, statement), getattr(facit, statement), sep=',', file=f)

