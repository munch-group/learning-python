
import sys, os
import importlib
import shelve
import random
import textwrap
import csv
import time
import datetime
from collections import defaultdict

random.seed(7)

_, bioinf_facit_file_name, bioinf_answer_file_name, output_shelve_file_name = sys.argv

# read exam questions from facit file
sys.path.append('.')
facit_basename = os.path.splitext(os.path.split(bioinf_facit_file_name)[1])[0]
facit_module = __import__(facit_basename)

# open shelve
output_db = shelve.open(output_shelve_file_name)

with open(bioinf_answer_file_name) as input_file:

    # read in student answers
    csv_reader = csv.reader(input_file, delimiter=',')
    lines = []
    for row in csv_reader:
        stud_id, question_name, answer, facit = row
        # if facit == "<class 'str'>":
        if facit not in ['True', 'False']:
            try:
                float(facit)
            except:
                print(facit)
                lines.append((stud_id, question_name, answer, facit ))

    # print questions and answers and prompt for score

    groups = defaultdict(list)
    for line in lines:
        groups[line[1]].append(line)
    new_lines = []
    for group in groups:
        random.shuffle(groups[group])
        new_lines.extend(groups[group])
    lines = new_lines
#    random.shuffle(lines)

    graded_keys = []
    i = 0
    then = time.time()
    times = []
    while i < len(lines):
        
        try:
            stud_id, question_name, answer, facit = lines[i]

            # db key
            key = f'{stud_id} {question_name}'

            # skip graded answers
            if key in output_db:
                i += 1
                continue
            
            # how much time is left
            min_remaining = ''
            if times:
                seconds_left = int((len(lines) - len(output_db)) * sum(times)/len(times))
                conversion = datetime.timedelta(seconds=seconds_left)
                min_remaining = f' (done in {conversion})'

            # extract exam question text
            print(getattr(facit_module, question_name))
            question_test = 'Q: ' + getattr(facit_module, question_name)

            # prompt
            question = '\n'.join(textwrap.wrap(question_test, width=60)) 
            progress = f"({len(output_db)}/{len(lines)}): " + '-'*55 + min_remaining
            answer_text = '\n'.join(textwrap.wrap('A: ' + answer, width=60)) 
            prompt_text = "Points (0/1): "
            points = input('\n' + progress + '\n\n' + question + '\n\n' + answer_text + '\n\n' + prompt_text)
            while points not in ['0', '1']:
                points = input(prompt_text)
            points = int(points)

            # update db and keys graded in this session
            output_db[key] = points
            graded_keys.append(key)

        except KeyboardInterrupt:
            try:
                s = input("\nGo back (int) grades or continue? (Ctrl-C again to exit): ")
                try:
                    back = min(int(s), len(graded_keys))
                    i -= back
                    print(i)
                    for b in range(back):
                        del_key = graded_keys.pop()
                        del output_db[del_key]
                    output_db.sync()
                    continue
                except ValueError:
                    continue
            except KeyboardInterrupt:
                output_db.sync()
                sys.exit()

        i += 1
        now = time.time()
        times.append(now - then)
        then = now

# write csv file with result
f = csv.writer(open(output_shelve_file_name + '.csv', 'w'))
for key in output_db:
    student_id, question_label = key.split()
    f.writerow([student_id, question_label, output_db[key]])

