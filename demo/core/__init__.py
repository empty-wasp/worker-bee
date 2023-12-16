from conf.record import Record
from conf.execute import Execute
from threading import Thread
from pynput.keyboard import Controller, Key

from conf.utils import getFileList, delFile
from time import sleep
from os.path import exists, isfile
from os import remove

keyboard = Controller()
record = Record()
execute = Execute()


class SuperWorkerBee:
    def __init__(self, sg, win):
        self.window = win
        self.psg = sg

    def recordStart(self, values):
        '开始录制'
        if bool(values['-RECORD-']):
            self.window['-RECORDBTN-'].update(disabled=True)
            self.window.Refresh()
            self.monitorThread(values, self.window)
        else:
            self.psg.popup_ok("Tips:", "请输入录制文件名称")

    def recordStop(self):
        '停止录制'
        keyboard.press(Key.delete)
        sleep(0.01)
        keyboard.release(Key.delete)

    def executeStart(self, values):
        '执行文件'
        file = values['-PLAY-'] or 'default.json'
        if values['-DELAY-'][-1] in ('0123456789'):
            self.delay = int(values['-DELAY-'])
        if exists('json/'+file):
            if values['-NUM-'][-1] in ('0123456789'):
                num = int(values['-NUM-'])
                if num:
                    self.window['-INDEX-'].update(value='播放开始')
                    self.window.Refresh()
                    self.operationThread(
                        values, num, self.delay, self.window)
            else:
                self.psg.popup_ok("Tips:", "请输入正确循环次数")
        else:
            self.psg.popup_ok("Error:", "播放文件不存在")

    def executeStop(self):
        '停止执行'
        execute.stop()

    def delFile(self, values):
        '删除单个文件'
        del_file = 'json/' + values['-PLAY-']
        if (isfile(del_file)):
            remove(del_file)
            self.psg.popup_ok("Success:", "删除成功")
            recordList = getFileList('json')
            self.window['-PLAY-'].update(values=recordList)
            self.window.Refresh()
        else:
            self.psg.popup_ok("Tips:", "文件不存在")

    def resetFile(self):
        '删除全部文件'
        delFile('json')
        self.window['-PLAY-'].update(values='')
        self.window.Refresh()

    def monitorThread(self, values, win):
        '创建监听子线程'
        def init(v, w):
            record.start(v['-RECORD-'], w)
            file_list = getFileList('json')
            self.window['-PLAY-'].update(values=file_list)
        Thread(target=init, args=[values, win]).start()

    def operationThread(self, values, num, delay, win):
        '创建播放子线程'
        def init(v, n, d, w):
            execute.start(v['-PLAY-'], n, d, w)
        Thread(target=init, args=[values, num, delay, win]).start()
