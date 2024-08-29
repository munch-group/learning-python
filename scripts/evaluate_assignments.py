"""
A tool for running tests on assignment files downloaded from Blackboard and from Digital Examen

Author: Dan Søndergaard <das@birc.au.dk>
Date: 15/12/2016
"""

import argparse
import shutil
import subprocess
import sys
import os
from pathlib import Path
import patoolib
import yaml
import argparse
import re
from collections import defaultdict

PROJECTS = None

ESC_TRANS = str.maketrans({"-":  r"\-", " ":  r"\ "})

def copy_file(from_path, to_path):
    shutil.copy(str(from_path), str(to_path))


def copy_tree(from_path, to_path):
    shutil.copytree(str(from_path), str(to_path))


def remove_tree(path):
    shutil.rmtree(str(path))


def find_assignment_file(wd, prefix):
    for path in wd.iterdir():
        if path.is_dir() or path.suffix == '.txt':
            continue
        if path.match('{}*'.format(prefix)):
            return path
    return None


def move_or_unpack_assignment_file(assignment_file, out_dir, project_name):
    if assignment_file.suffix == '.py':
        copy_file(assignment_file, out_dir / '{}.py'.format(project_name))
    elif assignment_file.suffix in ['.zip', '.rar']:
        patoolib.extract_archive(
            str(assignment_file),
            outdir=str(out_dir),
            verbosity=-1,
            interactive=False)

        # Move unpacked files to root assignment dir.
        for path in out_dir.glob('**/*.py'):
            if path.parent != out_dir:
                copy_file(path, out_dir)
    else:
        raise Exception('Assignment file not found!' + str(assignment_file))


def read_student_name(ident_file):
    text = ident_file.read_text(encoding='utf8')
    first_line = text.splitlines()[0]
    tokens = first_line.split(':', 1)
    return tokens[1].strip()


def run_tests(test_file, assignment_dir):
    cmd = 'GRADE_MODE=1 python {}'.format(test_file)
    process = subprocess.run(
        cmd,
        cwd=str(assignment_dir),
        shell=True,
        universal_newlines=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    # return process.returncode == 0 and 'skipped' not in process.stdout
    return process.returncode, process.stdout, process.stderr


def check_project(wd, failed_dir, student_name, student_file, project_name, overwrite, ta_suffix=''):
    project = PROJECTS[project_name]

    project_dir = student_file.with_suffix('')

    # a file for TA notes
    if ta_suffix:
        ta_note_file = student_file.with_suffix('.{}.txt'.format(ta_suffix))
    else:
        ta_note_file = student_file.with_suffix('.txt')
    ta_note_file.touch(exist_ok=True)

    assignment_file = find_assignment_file(wd, project_dir)
    if assignment_file is None:
        print('ERROR: Did not find assignment file in', project_dir)
        sys.exit()

    if assignment_file is not None: 

        project_dir.mkdir(exist_ok=True)
        assignment_file_orig = project_dir / Path('original').with_suffix(assignment_file.suffix)
        
        if not assignment_file_orig.exists() or overwrite:

            copy_file(assignment_file, assignment_file_orig)
            move_or_unpack_assignment_file(assignment_file, project_dir, project_name)

    # if assignment_file is not None and (not project_dir.exists() or overwrite):

    #     project_dir.mkdir(exist_ok=True)

    #     assignment_file_orig = project_dir / Path('original').with_suffix(assignment_file.suffix)

    #     copy_file(assignment_file, assignment_file_orig)
    #     move_or_unpack_assignment_file(assignment_file, project_dir, project_name)


    for from_path, to_path in project['files'].items():
        copy_file(from_path, project_dir / to_path)

    # has_passed = run_tests(project['test_file'], project_dir)
    # if not has_passed:
    #     print('FAILED', student_name.encode())
    #     copy_tree(project_dir, failed_dir / project_dir.name)
    # else:
    #     print('OK    ', student_name.encode())
    script_return_status, script_output, script_stderr = run_tests(project['test_file'], project_dir)

    if script_return_status == 99: # error during import of student code
        # print('IMPORTERROR', ta_suffix, student_name, "\n\t", str(project_dir / "{}.py".format(project_name)).translate(ESC_TRANS))
        # print('IMPORTERROR', ta_suffix, student_name, "\n\t", str(project_dir).translate(ESC_TRANS))
        print(ta_suffix, 'IMPORTERROR', student_name, "\n\t", str(project_dir).translate(ESC_TRANS))
        import_error_file = project_dir / 'import_error.txt'        
        with open(str(import_error_file), 'w') as f:
            print(script_output, file=f)

        if ta_suffix:
            ta_failed_dir = failed_dir / ta_suffix
            ta_failed_dir.mkdir(exist_ok=True)
            copy_tree(project_dir, ta_failed_dir / project_dir.name)
            copy_file(ta_note_file, ta_failed_dir / ta_note_file.name)
            # copy_file(student_file, ta_failed_dir / student_file.name)
            copy_file(import_error_file, ta_failed_dir / import_error_file.name)
        else:
            copy_tree(project_dir, failed_dir / project_dir.name)
            copy_file(ta_note_file, failed_dir / ta_note_file.name)
            # copy_file(student_file, failed_dir / student_file.name)
            copy_file(import_error_file, failed_dir / import_error_file.name)


    elif script_return_status or 'skipped' in script_stderr:
        # print('FAILED', ta_suffix, student_name)
        print(f'{ta_suffix:<25}',  f'{"FAILED":<7}', student_name)

        if ta_suffix:
            ta_failed_dir = failed_dir / ta_suffix
            ta_failed_dir.mkdir(exist_ok=True)
            copy_tree(project_dir, ta_failed_dir / project_dir.name)
            copy_file(ta_note_file, ta_failed_dir / ta_note_file.name)
            # copy_file(student_file, ta_failed_dir / student_file.name)
        else:
            copy_tree(project_dir, failed_dir / project_dir.name)
            copy_file(ta_note_file, failed_dir / ta_note_file.name)
            # copy_file(student_file, failed_dir / student_file.name)

    else:
        # print('PASSED', ta_suffix, student_name)
        print(f'{ta_suffix:<25}', f'{"OK":<7}', student_name)

    return project_dir / 'test_progexam.csv'

def get_ta_suffix(ta_classes, student_name):

    actual_student_name = re.match(r'[^()]+', student_name).group(0).strip()
    if ta_classes is None:
        return ""
    else:
        ta_labels = list()
        for label, class_participants in ta_classes.items():
            if actual_student_name in class_participants.values():
                ta_labels.append(label)
        if not ta_labels:
            return "NO-TA-ASSIGNED"
        else:
            return "-".join(ta_labels)


# def check_assignments(assignment_dir, project_name, overwrite, ta_classes=None):
#     failed_dir = assignment_dir / 'failed'
#     if failed_dir.exists():
#         remove_tree(failed_dir)
#     failed_dir.mkdir(exist_ok=True)

#     import_error_dir = assignment_dir / 'import_error'
#     if import_error_dir.exists():
#         remove_tree(import_error_dir)
#     import_error_dir.mkdir(exist_ok=True)

#     student_files = [(read_student_name(student_file), student_file)
#                      for student_file in assignment_dir.glob('*[0-9][0-9]-[0-9][0-9]-[0-9][0-9].txt')]

#     for student_name, student_file in sorted(student_files):
#         ta_suffix = get_ta_suffix(ta_classes, student_name)
#         check_project(assignment_dir, failed_dir, student_name, student_file, 
#             project_name, overwrite, ta_suffix=ta_suffix)


def check_bioinf_answers(assignment_dir, student_file, student_name, project_name, overwrite):
    project = PROJECTS[project_name]

    project_dir = student_file.with_suffix('')
    student_file_copy = project_dir / 'bioinf.py'
    student_file_original = project_dir / 'original.py'

    if not project_dir.exists() or overwrite:
        project_dir.mkdir(exist_ok=True)
        copy_file(student_file, student_file_copy)
        copy_file(student_file, student_file_original)

    facit_file = project['bioinf_facit_file']
    facit_script = project['bioinf_facit_script']

    output_file_name = student_file_copy.with_suffix('.csv')

    cmd = ['python', str(facit_script), str(facit_file), str(student_file_copy), str(output_file_name)]

    process = subprocess.run(
        cmd,
        shell=False,
        universal_newlines=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

    return_code = process.returncode    
    stdout = process.stdout
    stderr = process.stderr
    if return_code or stdout or stderr:        
        print("####################################################################")
        print("Problem with: ", str(student_file).translate(ESC_TRANS))
        print("Edit this copy of the student file:\n{}\n".format(str(student_file_copy).translate(ESC_TRANS)))
        print(stderr)
        print("####################################################################")
        sys.exit()

    return output_file_name


def main():

    description="""This script processes an unzipped archive of assignments downloaded from 
Backboard or Digital Exam and runs a specified test script on the assignments.
"""

    epilog="""To download the assignments from Blackboard click "Grade center" in
the left menu. Then click "Full grade center". In the table view there is a 
small dropdown in column header for the assignment you want to download 
(e.g. hivproject). In the dropdown menu you clid "Assignment file download". 
Then scroll down to the bottom and clidk "Show all". Then scroll up and tick
the top left box to select all. Then click "Submit". To then download the 
zipped archive you click "Download assignments now". Unpack this archive. 
The resulting directory is must be given as first argument to the script. 

You use the --data option to specify which (defualt is blackboard). The 
test_files and files required for each project are specified in the PROJECTS
specification in the main function. For both blackboard and digital exam 
assignments this script runs the test script with unit tests in GRADE_MODE.

For blackboard assignments the script unpacks the zip file for each student 
and moves the test and other required files input into each student dir. In the 
student dir the a copy of the student file python file is called original.py so
you can edit project.py without losing the original student version. The same
folder has an empty text file for notes on the student.

If the test script is unable to import the student code it will write an 
import_error.txt in the student dir. For each student with import error, the error
causing the import error must me resolved manually by commenting out code causing 
it. Having resolved these errors this script must be run again.

For digital exam assignments the script works much the same way, but also parses
bioinformatics assignments (see README.md in exam_evaluation for details).
"""

    repo_dir = '/Users/kmt/google_drive/teaching/bop/bioinf-prog-course'

    global PROJECTS
    # The keys in PROJECTS must be the basenames of the files that the students produce.
    # I.e. the names of the modules that are imported by the test script.
    PROJECTS = {

        # Translate open reading frames
        'translationproject': {
            'test_file': 'test_translationproject.py',
            'files': {
                f'{repo_dir}/programming_projects/translationproject/test_translationproject.py': 'test_translationproject.py',
            }
        },

        # HIV sequence comparison
        'hivproject': { 
            'test_file': 'test_hivproject.py',
            'files': {
                f'{repo_dir}/programming_projects/hivproject/test_hivproject.py': 'test_hivproject.py',
                f'{repo_dir}/programming_projects/hivproject/subtypeA.txt': 'subtypeA.txt',
                f'{repo_dir}/programming_projects/hivproject/subtypeB.txt': 'subtypeB.txt',
                f'{repo_dir}/programming_projects/hivproject/subtypeC.txt': 'subtypeC.txt',
                f'{repo_dir}/programming_projects/hivproject/subtypeD.txt': 'subtypeD.txt',
                f'{repo_dir}/programming_projects/hivproject/unknown_type.txt': 'unknown_type.txt',
            }
        },

        # Codon bias project
        'codonbiasproject': {
            'test_file': 'test_codonbiasproject.py',
            'files': {
                f'{repo_dir}/programming_projects/codonbiasproject/test_codonbiasproject.py': 'test_codonbiasproject.py',
                f'{repo_dir}/programming_projects/codonbiasproject/sample_orfs.txt': 'sample_orfs.txt',
            }
        },

        # Sequence assembly
        'assemblyproject': { 
            'test_file': 'test_assemblyproject.py',
            'files': {
                f'{repo_dir}/programming_projects/assemblyproject/test_assemblyproject.py': 'test_assemblyproject.py',
                f'{repo_dir}/programming_projects/assemblyproject/sequencing_reads.txt': 'sequencing_reads.txt',
            }
        },

        # Predicting proteins
        'orfproject': { 
            'test_file': 'test_orfproject.py',
            'files': {
                f'{repo_dir}/programming_projects/orfproject/test_orfproject.py': 'test_orfproject.py',
                f'{repo_dir}/programming_projects/orfproject/e_coli_O157_H157_str_Sakai.fasta': 'e_coli_O157_H157_str_Sakai.fasta',
            }
        },

        # RNA folding
        'foldingproject': { 
            'test_file': 'test_foldingproject.py',
            'files': {
                f'{repo_dir}/programming_projects/foldingproject/test_foldingproject.py': 'test_foldingproject.py',
            }
        },

        'progexam': {
            'test_file': 'test_progexam.py',
            'files': {
                os.path.abspath('../test_progexam.py'): 'test_progexam.py',
            },
            'bioinf_facit_file': os.path.abspath('../bioinformatics_facit.py'),
            'bioinf_facit_script': os.path.abspath('../check_bioinfexam.py'),
        },

    }


    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=description, 
                                     epilog=epilog)

    parser.add_argument("--overwrite", 
                        action="store_true", 
                        default=False,
                        help="Redo unpacking and copying of test and input files")
    parser.add_argument('--ta-classes',
                       dest="ta_classes",
                       type=Path,
                       help='Path to yaml file with students divided in to classes.')
    parser.add_argument('--data',
                        choices=['brightspace', 'blackboard', 'digitalexam'],
                        default='brightspace',
                        help='Type of data to parse')
    parser.add_argument('assignment_dir', 
                        type=Path,
                        help='path to gradebook directory downloaded from Blackboard')
    parser.add_argument('project_name',
                        choices=PROJECTS.keys(),
                        help='Name of the project to test.')

    args = parser.parse_args()

    if not args.assignment_dir.exists():
        print('The directory does not exist {}'.format(args.assignment_dir))
        sys.exit()

    args.assignment_dir = args.assignment_dir.resolve()

    if args.ta_classes:
        ta_classes = yaml.load(open(str(args.ta_classes)), Loader=yaml.FullLoader)

        # to accomodate new format with info pasted from groups on Brightspace:
        for ta_class in ta_classes:
            name_list = []
            id_list = []
            for student_info in ta_classes[ta_class]:
                last, first, auid, rawauid = student_info.split(', ')
                name_list.append(f'{first} {last}')
                id_list.append(auid)
            ta_classes[ta_class] = dict(zip(id_list, name_list))

    else:
        ta_classes = None

    failed_dir = args.assignment_dir / 'failed'
    if failed_dir.exists():
        remove_tree(failed_dir)
    failed_dir.mkdir(exist_ok=True)

    import_error_dir = args.assignment_dir / 'import_error'
    if import_error_dir.exists():
        remove_tree(import_error_dir)
    import_error_dir.mkdir(exist_ok=True)

    if args.data == 'blackboard':
        student_files = [(read_student_name(student_file), student_file)
                         for student_file in args.assignment_dir.glob('*[0-9][0-9]-[0-9][0-9]-[0-9][0-9].txt')]

        for student_name, student_file in sorted(student_files):
            project_dir = student_file.with_suffix('')
            assignment_file = find_assignment_file(args.assignment_dir, project_dir)
            file_structure_ok = True
            if assignment_file is None:
                with open(str(student_file)) as f:
                    if 'No files were attached to this submission' in f.read():
                        student_files.remove((student_name, student_file))
                    else:
                        print('No student file for {} in {}'.format(student_name, project_dir))
                        file_structure_ok = False
            if not file_structure_ok:
                print('FIX FILE STRUCTURE AND RERUN')
                sys.exit()

        for student_name, student_file in sorted(student_files):
            ta_suffix = get_ta_suffix(ta_classes, student_name)
            check_project(args.assignment_dir, failed_dir, student_name, student_file, 
                args.project_name, args.overwrite, ta_suffix=ta_suffix)


    elif args.data == 'brightspace':

        student_files = []
        for path in args.assignment_dir.glob('[0-9]*'):
            if not path.is_dir():
                continue
            student_name = re.search(r'- (.+) -', path.name).group(1)
            student_files.append((student_name, path.with_suffix('.txt')))

            # Hack to make the file structure the same as blackboard:
            copy_from = path / f'{args.project_name}.py'
            copy_to = path.parent / f'{path.stem}_{args.project_name}.py'
            if copy_from.exists():
                copy_file(copy_from, copy_to)

        for student_name, student_file in sorted(student_files):
            project_dir = student_file.with_suffix('')
            assignment_file = find_assignment_file(args.assignment_dir, project_dir)
            file_structure_ok = True
            # if assignment_file is None:
            #     with open(str(student_file)) as f:
            #         if 'No files were attached to this submission' in f.read():
            #             student_files.remove((student_name, student_file))
            #         else:
            #             print('No student file for {} in {}'.format(student_name, project_dir))
            #             file_structure_ok = False
            # if not file_structure_ok:
            #     print('FIX FILE STRUCTURE AND RERUN')
            #     sys.exit()

        for student_name, student_file in sorted(student_files):
            ta_suffix = get_ta_suffix(ta_classes, student_name)
            try:
                check_project(args.assignment_dir, failed_dir, student_name, student_file, 
                    args.project_name, args.overwrite, ta_suffix=ta_suffix)                
            except KeyboardInterrupt:
                print()
                print(os.path.dirname(student_file))
                print()
                raise

    else:
        # digital exam

        import PyPDF2 # for reading meta info file on student

        def get_student_id_from_pdf(file_name):
            pdfFileObj = open(file_name,'rb')     #'rb' for read binary mode
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            #pdfReader.numPages
            pageObj = pdfReader.getPage(0)          #'9' is the page number
            text = pageObj.extractText()
            # student_id = re.search(r'(\d+)@post.au.dk', text).group(1)
            student_id = re.search(r'Besvarelsen afleveres af\n(\d+)', text).group(1)
            assert student_id
            return student_id

        prog_result_files = list()
        bioinf_result_files = list()

        with open(str(args.assignment_dir / 'student_list.csv'), 'w') as student_csv_file:

            for path in args.assignment_dir.glob('*.pdf'):

                student_id = get_student_id_from_pdf(str(path))

                student_name, student_exam_id, hand_in_id, _cover_page, _suf = path.name.split('_')
                assert _cover_page == 'Forside'

                # compile stud regex to solve stupid problem:
                # There are unicode characters in the student names that are
                # sometimes one unicode character and sometimes two:
                # >>> len('Å')
                # 2
                # >>> len('Å')
                # 1
                # >>>
                stud_regex = re.compile(''.join(x if x.isascii() else '..?' for x in student_name) + f'_{student_exam_id}')

                student_row = [student_id, student_name] 

                # get prog exam file
                lst = [f for f in args.assignment_dir.glob('*progexam.py') if stud_regex.search(str(f))]
                # lst = list(args.assignment_dir.glob('{}_{}*{}.py'.format(student_name, student_exam_id, args.project_name)))
                assert len(lst) <= 1, lst
                if len(lst) == 1:
                    progexam_file = lst[0]
                    # student_row.append('handin')
                    student_row.extend(['handin', progexam_file])
                    result_file = check_project(args.assignment_dir, failed_dir, student_name, progexam_file, 
                        args.project_name, args.overwrite)
                    prog_result_files.append((student_id, result_file))
                else:
                    # student_row.append('missing')
                    print("MISSING PROGRAMMING FILE: {} (copy orig file to version with correct name)\n\t{}".format(student_name,
                        str(args.assignment_dir / student_name).translate(ESC_TRANS)), file=sys.stderr)
                    student_row.extend(['missing', None])

                # get bioinf exam file

                lst = [f for f in args.assignment_dir.glob('*bioinfexam.py') if stud_regex.search(str(f))]
                # lst = list(args.assignment_dir.glob('{}_{}*bioinfexam.py'.format(student_name, student_exam_id)))
                assert len(lst) <= 1, lst
                if len(lst) == 1:
                    bioinfexam_file = lst[0]
                    #student_row.append('handin')
                    student_row.extend(['handin', bioinfexam_file])
                    result_file = check_bioinf_answers(args.assignment_dir, bioinfexam_file, student_name, args.project_name, args.overwrite)
                    bioinf_result_files.append((student_id, result_file))
                else:
                    #student_row.append('missing')
                    print("MISSING BIOINF FILE: {} (copy orig file to version with correct name)\n\t{}".format(student_name, 
                        str(args.assignment_dir / student_name).translate(ESC_TRANS)), file=sys.stderr)
                    student_row.extend(['missing', None])

                print(*student_row, sep=',', file=student_csv_file)

        # collect all prog answers
        with open(str(args.assignment_dir / 'prog_hand_in_summary.csv'), 'w') as csv_file:
            for student_id, path in prog_result_files:
                if path.exists():
                    with open(str(path)) as f:
                        for l in f:
                            print("{},{}".format(student_id, l.strip()), file=csv_file)

        # collect all bioinf answers
        with open(str(args.assignment_dir / 'bioinf_hand_in_summary.csv'), 'w') as csv_file:
            for student_id, path in bioinf_result_files:
                if path.exists():
                    with open(str(path)) as f:
                        for l in f:
                            print("{},{}".format(student_id, l.strip()), file=csv_file)



if __name__ == "__main__":
    main()

# python evaluate_assignments.py --ta-classes class_participants.yaml mandatory_assignments/assemblyproject/gradebook_BB-Cou-UUVA-69396_Project3a20Genome20assembly_2017-11-01-10-12-36 assemblyproject > mandatory_assignments/assemblyproject/AP_student_status.txt


