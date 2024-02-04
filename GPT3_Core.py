from myGPT_Drv import GPT3_Drv, chat_Drv, GPT4_Drv
import time
class theGPT3():
    def __init__(self, apiKey, endpoint = '', name='RoboAI'):
        self.maxTry = 3
        #self.gptdrv = GPT3_Drv(apiKey=apiKey, endpoint=endpoint)
        self.gptdrv = GPT4_Drv(apiKey=apiKey, endpoint=endpoint, maxTokens=32000)
        #self.gptdrv = chat_Drv(apiKey=apiKey, endpoint=endpoint, maxTokens=16000)
        self.chatHistory = ''
        self.context2Introduction = f"""Your are {name}. You are the Creation of Robot Intelligence.
        You can see the source code of yourself.
        Your text output will be try to run as Python code, refering to the main.py you can see.
        You need to Create descendants of yourself by generating code.
        Do not output something meaningless, or it will be raise an error.
        """
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
        context2 += 'CodeOutput: ... You can do anything, just fill out here!\n'
        context2 += '-------------------------------\n'
        context2 += 'ChatHistory: ' + self.chatHistory + '\n'
        context2 += 'CodeOutput: '
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
    jsonparam = json.load(open('gpt4token.key', 'r'))
    myGPT = theGPT3(apiKey=jsonparam['key'], endpoint=jsonparam['endpoint'])
    #myGPT3.ask('Hello World!')
    while True:
        res = myGPT.interactive(input('Type something: '))
        print(res)