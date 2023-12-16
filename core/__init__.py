#!/usr/bin/env python3
from pynput.keyboard import Controller, Key
from threading import Thread
from tkinter import messagebox as msg
from time import sleep
from .style import Style
from .record import Record
from .play import Play

keyboard = Controller()

record = Record()
play = Play()


class Interface(Style):

    def __init__(self, root):
        super().__init__(root)
        self.RECORD_COMP(self.__RECORD, self.__RECORD_STOP)
        self.PLAY_COMP(self.__PLAY, self.__PLAY_stop)

    def __RECORD(self):
        try:
            self.SET_RTEXT('录制中')
            record_th = Thread(target=record.start, args=[self.SET_RTEXT])
            record_th.start()
        except Exception as e:
             msg.showinfo(title='ERROR', message=e)

    def __RECORD_STOP(self):
        '停止录制'
        keyboard.press(Key.delete)
        sleep(0.01)
        keyboard.release(Key.delete)

    def __PLAY(self):
        '开始播放'
        try:
            if self.GET_LOOP() and self.GET_DELAY():
                self.SET_PTEXT('STATE')
                play_th = Thread(target=play.start, args=[
                    self.SET_PTEXT, self.GET_LOOP, self.GET_DELAY])
                play_th.start()
        except Exception as e:
            msg.showinfo(title='ERROR', message=e)

    def __PLAY_stop(self):
        '停止播放'
        play.stop()
