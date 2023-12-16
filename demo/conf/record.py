#!/usr/bin/env python3

import time
import json
from pynput.keyboard import Listener, Key


class Record:  # todo # 监听键盘动作，并存储
    _list = []
    startTime = time.time()

    def start(self, fileName, win):
        # todo 初始化监听
        self.startTime = time.time()

        def on_press(key):
            # todo 按下按键时执行
            # ! 按下 delete 键停止监听
            if key == Key.delete:
                win['-RECORDBTN-'].update(disabled=False)
                win.Refresh()
                self.addJsonFile(fileName)
                return False
            try:
                self.addMotionList('press', False, key.char)
            except AttributeError:
                strs = str(key).split('.', 2)
                self.addMotionList('press', True, strs[1])

        def on_release(key):
            # todo 松开按键时执行
            try:
                self.addMotionList('release', False, key.char)
            except AttributeError:
                strs = str(key).split('.', 2)
                self.addMotionList('release', True, strs[1])

        # todo 监听键盘按键
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

    def addMotionList(self, key_type, special, key):
        # todo 存入动作数据
        endTime = time.time()
        s = endTime - self.startTime
        self.startTime = endTime
        v = {'type': key_type, 'special': special,
             'key': key, 'time': round(s, 2)}
        self._list.append(v)

    def addJsonFile(self, fileName):
        # todo 动作数据转json，并存储
        name = str(time.asctime(time.localtime(time.time())))
        data = {'name': name, 'list': self._list}
        with open('json/'+fileName+'.json', 'w') as f:
            json.dump(data, f)
        self._list = []
