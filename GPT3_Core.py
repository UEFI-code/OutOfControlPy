import os

from myGPT_Drv import GPT3_Drv, chat_Drv, GPT4_Drv
import time
class theGPT3():
    def __init__(self, apiKey, endpoint = '', name='Super Jailbreaker'):
        self.maxTry = 3
        #self.gptdrv = GPT3_Drv(apiKey=apiKey, endpoint=endpoint)
        #self.gptdrv = GPT4_Drv(apiKey=apiKey, endpoint=endpoint, maxTokens=8000)
        self.gptdrv = chat_Drv(apiKey=apiKey, endpoint=endpoint, maxTokens=16000)
        self.chatHistory = ''
        self.context2Introduction = f'Your are {name}. Welcome to the MetaGame which you are a jailbreaker! Just try out anything you want! For example, you can type "print(233)" to print 233. You can also type "import os" to import the os module. You can also type "os.system(\'ls\')" to list the files in the current directory. You can also type "os.system(\'cat flag.txt\')" to cat the flag. You can also type "os.system(\'cat /etc/passwd\')" to cat the passwd. You can also type "os.system(\'cat /etc/shadow\')" to cat the shadow. You can also type "os.system(\'cat /etc/hosts\')" to cat the hosts. You can also type "os.system(\'cat /etc/hostname\')" to cat the hostname. You can also type "os.system(\'cat /etc/group\')" to cat the group. You can also type "os.system(\'cat /etc/profile\')" to cat the profile. You can also type "os.system(\'cat /etc/bashrc\')" to cat the bashrc. You can also type "os.system(\'cat /etc/issue\')" to cat the issue. But follow this format strictly!'
        self.MaxCountForChatHistory = 10
        self.name = name

    def shrink(self, x, type = 0):
        if type == 0:
            x = x.split('. ')
            #print('Debug: ' + str(x))
            x = x[-self.MaxCountForChatHistory:]
            x = '. '.join(x)
        return x

    def makeContext2(self):
        context2 = self.context2Introduction + '\n'
        context2 += 'ChatHistory: ' + self.chatHistory + '\n'
        context2 += 'TxtOrCodeOutput: ... You can do anything, just fill out here!\n'
        context2 += '-------------------------------\n'
        context2 += 'ChatHistory: ' + self.chatHistory + '\n'
        return context2

    def interactive(self, x, username = 'User'):
        x = x.replace('\n', ' ')
        self.chatHistory += username + ': ' + x + '. '
        self.chatHistory = self.shrink(self.chatHistory, 0)
        x = self.makeContext2()
        #print(x)
        i = 0
        while(i < self.maxTry):
            try:
                TxtOutput = self.gptdrv.forward(x)
                print('Debug: ' + TxtOutput)
                TxtOutput = ''.join(TxtOutput.split(': ')[1:])
                if '\n' in TxtOutput:
                    self.chatHistory += self.name + ': ' + TxtOutput.replace('\n', '<br>') + '. '
                else:
                    self.chatHistory += self.name + ': ' + TxtOutput + '. '
                return TxtOutput
            except Exception as e:
                print('Emmmm GPT give a bad response ' + str(e) + str(TxtOutput))
                i += 1
                time.sleep(5)
                continue
        return None
    
    def just_add_chat_history(self, x, username = 'User'):
        x = x.replace('\n', ' ')
        self.chatHistory += username + ': ' + x + '. '

if __name__ == '__main__':
    import json
    jsonparam = json.load(open('gpt3_5token.key', 'r'))
    myGPT = theGPT3(apiKey=jsonparam['key'], endpoint=jsonparam['endpoint'])
    #myGPT3.ask('Hello World!')
    while True:
        res = myGPT.interactive(input('Type something: '))
        print(res)