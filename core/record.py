#!/usr/bin/env python3
from pynput.keyboard import Listener, Key
from threading import Thread
from time import time
from json import dump


class Record:
    '监听键盘动作，并存储'
    __LIST = []
    __STIME = None
    __ETIME = None

    def start(self, SET_RTEXT):
        '执行监听线程'
        self.__STIME = time()
        self.watch_th = Thread(target=self.watch_thread, args=[SET_RTEXT])
        self.watch_th.start()

    def watch_thread(self, SET_RTEXT):
        '执行监听'
        def on_press(key):
            '按下按键时执行'
            if key == Key.delete:   # ! 按下 delete 键停止监听
                with open('assets/default.json', 'w') as f:
                    dump(self.__LIST, f)
                self.__LIST = []
                SET_RTEXT('停止监听')
                return False

            try:
                self.__ADDMOTION('press', False, key.char)
            except AttributeError:
                strs = str(key).split('.', 2)
                self.__ADDMOTION('press', True, strs[1])

        def on_release(key):
            '松开按键时执行'
            try:
                self.__ADDMOTION('release', False, key.char)
            except AttributeError:
                strs = str(key).split('.', 2)
                self.__ADDMOTION('release', True, strs[1])

        # todo 监听键盘按键
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

    def __ADDMOTION(self, t, spc, k):
        '存入动作数据'
        self.__ETIME = time()
        timer = self.__ETIME - self.__STIME
        self.__STIME = self.__ETIME
        v = {'type': t, 'special': spc, 'key': k, 'time': round(timer, 2)}
        self.__LIST.append(v)
