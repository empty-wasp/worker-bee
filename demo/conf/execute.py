#!/usr/bin/env python3

import time
import json

from pynput.keyboard import Controller, Key
keyboard = Controller()


class Execute:  # todo 获取工作数据，并播放
    flag = False

    def start(self, fileName, num, delay, win):
        # todo 初始化动作，获取数列表
        self.flag = False
        with open('json/'+fileName, 'r') as f:
            data = json.load(f)
        ls = data['list']
        n = 0
        for i in range(num):
            n += 1
            time.sleep(delay)
            v = '第' + str((i + 1)) + '次'
            win['-INDEX-'].update(value=v)
            win.Refresh()
            self.motion(ls)
            if (n == len(range(int(num)))):
                win['-INDEX-'].update(value='播放完成')
                win.Refresh()

    def press(self, v):
        # todo 按键按下
        if (v['special']):
            time.sleep(v['time'])
            keyboard.press(Key[v['key']])
        else:
            time.sleep(v['time'])
            keyboard.press(v['key'])

    def release(self, v):
        # todo 按键释放
        if (v['special']):
            time.sleep(v['time'])
            keyboard.release(Key[v['key']])
        else:
            time.sleep(v['time'])
            keyboard.release(v['key'])

    def motion(self, data):
        # todo 开始循环播放动作
        for v in data:
            if self.flag:
                break

            if v['type'] == 'press':
                self.press(v)
            else:
                self.release(v)

    def stop(self):
        self.flag = True
