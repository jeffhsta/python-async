from twisted.internet import reactor, defer, threads
from twisted.internet.task import LoopingCall
from time import sleep


def myprint(content):
    print(content)

def print_async(number):
    def wrapper():
        return str(number)

    d = threads.deferToThread(wrapper)
    d.addCallback(myprint)


def start():
    print('[*] asyncapp started!')

    # LoopingCall(callback_print, 'Duck').start(.25)
    [print_async(n) for n in range(10)]
    threads.deferToThread(lambda: reactor.stop())

    print('[*] waiting to finish the defers')
    reactor.run()
    print('[*] Finish the app!')
