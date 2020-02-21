import os
import random
import string
from src import db
import json

def run(code,input,ext):
    fcode, finput = create_files(code, input, ext)

    foutput = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 7)) + ".txt" 

    os.system(get_command(fcode, finput, foutput, ext))

    with open(foutput, "r") as f:
        data = f.read()

    delete_files(fcode, finput, foutput)

    return data
    
def get_command(fcode,finput,foutput,ext):
    if ext == '.py':
        return "python " + fcode + " < " + finput + " > " + foutput
    elif ext == '.cpp':
        return "g++ " + fcode + " && ./a.out < " + finput + " > " + foutput
    elif ext == ".c":
        return "gcc " + fcode + " && ./a.out < " + finput + " > " + foutput

def create_files(code, input_file, ext):
    fcode = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 7)) 
    fcode += ext
    finput = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 7))
    finput += ".txt"

    with open(fcode, "w") as f:
        f.write(code)
    
    with open(finput, "w") as f:
        f.write(input_file)

    return (fcode,finput)

def extract_extension(filename):
    return os.path.splitext(filename)[1]

def delete_files(fcode,finput, foutput):
    os.remove(fcode) 
    os.remove(finput)
    os.remove(foutput)

def run_testcases(file_id, parent):
    testcases = json.loads(db.load_testcases(file_id))
    new_testcases = []
    file_content, filename = db.get_file_content_from_id(file_id)
    for test in testcases:
        out = run(file_content,test[2],extract_extension(filename))
        if out.strip() == test[3].strip():
            db.change_testcase_status(test[0],1)   # 2 means right
            test[-1] = 1
        else :
            db.change_testcase_status(test[0],2)   # 2 means wrong
            test[-1] = 2
        new_testcases.append(test)
    return json.dumps(new_testcases)
        
