import glob
# Get all .py files in the current directory
py_files = glob.glob("*.py")

HackViewIntroduction = """These are the source code of your self!"""

for py_file in py_files:
    HackViewIntroduction += f"\n{py_file}:\n{open(py_file, 'r').read()}\n"

#print(HackViewIntroduction)

from GPT3_Core import theGPT3

if __name__ == '__main__':
    import json
    jsonparam = json.load(open('gpt3_5token.key', 'r'))
    myGPT = theGPT3(apiKey=jsonparam['key'], endpoint=jsonparam['endpoint'])
    myGPT.context2Introduction = HackViewIntroduction + myGPT.context2Introduction
    #myGPT3.ask('Hello World!')
    
    while True:
        sys_last_run_res = ''
        gptRes = myGPT.interactive(input('Type something: '))
        print(f'Debug: GPT Response {gptRes}')
        try:
            # Run the code that GPT generated
            exec(gptRes)
            sys_last_run_res += f'Code Run Successfull. '
        except Exception as e:
            sys_last_run_res += f'Code Run Failed: {e}. '
        myGPT.just_add_chat_history(sys_last_run_res, username='System')
