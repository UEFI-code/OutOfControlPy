import glob
import time
# Get all .py files in the current directory
py_files = glob.glob("*.py")

HackViewIntroduction = """These are the source code of your self!\n"""

for py_file in py_files:
    HackViewIntroduction += f"{py_file}:\n{open(py_file, 'r').read()}\n-------------------------------\n"

from GPT3_Core import theGPT3
import json

if __name__ == '__main__':
    jsonparam = json.load(open('gpt4token.key', 'r'))
    myGPT = theGPT3(apiKey=jsonparam['key'], endpoint=jsonparam['endpoint'])
    myGPT.context2Introduction = HackViewIntroduction + myGPT.context2Introduction

    gptRes = myGPT.interactive("""Hello World!, Lets begin to creating your future!
    You can do the patch work of the source code of yourself. 
    For example, you can run open('main.py', 'r').read().replace('import json', 'import json\nimport sys').write('main2.py') to add a new import in main2.py.
    Also, of course, you can try other commands. Finally, using os.system('python3 main2.py') to run the new code of yourself. Remember, output code only. No introduction, no ```python, don't do stupid things.
    """, username='System')
    
    while True:
        print(f'Debug GPT Response: {gptRes}')
        try:
            # Run the code that GPT generated
            exec(gptRes)
            sys_last_run_res = f'Code Run Successfull. '
        except Exception as e:
            sys_last_run_res = f'Code Run Failed: {e}. '
        print(f'Debug System Response: {sys_last_run_res}')
        time.sleep(5)
        myGPT.interactive(sys_last_run_res, username='System')