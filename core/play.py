#!/usr/bin/env python3
from pynput.keyboard import Controller, Key
from time import sleep
from json import load

keyboard = Controller()


class Play:  # todo 获取工作数据，并播放
    ___FLAG = False
    __LIST = None
    __LOOP = None
    __DELAY = None

    def start(self, SET_PTEXT, GET_LOOP, GET_DELAY):
        # todo 初始化动作，获取数列表
        self.___FLAG = False
        self.__LOOP = GET_LOOP()
        self.__DELAY = GET_DELAY()
        with open('assets/default.json', 'r') as f:
            self.__LIST = load(f)
        self.__MOTION(SET_PTEXT, 1)

    def stop(self):
        self.___FLAG = True

    def __PRESS(self, v):
        # todo 按键按下
        if (v['special']):
            sleep(v['time'])
            keyboard.press(Key[v['key']])
        else:
            sleep(v['time'])
            keyboard.press(v['key'])

    def __RELEASE(self, v):
        # todo 按键释放
        if (v['special']):
            sleep(v['time'])
            keyboard.release(Key[v['key']])
        else:
            sleep(v['time'])
            keyboard.release(v['key'])

    def __MOTION(self, SET_PTEXT, IDX):
        # todo 开始循环播放动作
        if IDX > self.__LOOP or self.___FLAG:
            SET_PTEXT('END')
            return False
        sleep(self.__DELAY)
        SET_PTEXT('第' + str(IDX) + '次')
        for v in self.__LIST:
            if self.___FLAG:
                SET_PTEXT('END')
                break
            if v['type'] == 'press':
                self.__PRESS(v)
            else:
                self.__RELEASE(v)
        self.__MOTION(SET_PTEXT, IDX + 1)
