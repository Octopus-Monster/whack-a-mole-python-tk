import platform

class Tools(object):
    def __init__(self):
        super(Tools, self)

    def get_OSInfo(self, Path):
        if(platform.system()=='Windows'):
            print('Windows系统')
            newPath =  str(Path).replace('/','\\')
            return newPath
        elif(platform.system()=='Linux'):
            print('Linux系统')
            newPath =  str(Path).replace('\\','/')
            return newPath
        elif(platform.system()=='Darwin'):
            print('MacOS系统')
            newPath =  str(Path).replace('\\','/')
            return newPath
        else:
            print('其他系统')
            pass