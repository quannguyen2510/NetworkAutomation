import difflib

def find_difference(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        diff = difflib.unified_diff(f1.readlines(), f2.readlines(), fromfile=file1, tofile=file2)
        return '\n'.join(diff)

file1_path = r'D:\StudyCarrer\Capstone Project\Code\NetworkAutomation\Test\log1.txt'
file2_path = r'D:\StudyCarrer\Capstone Project\Code\NetworkAutomation\Test\log2.txt'

difference = find_difference(file1_path, file2_path)
print(difference)
