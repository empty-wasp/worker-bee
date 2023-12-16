#!/usr/bin/env python3
from tkinter import LabelFrame, Button, Label, Entry, RAISED
from tkinter import StringVar, IntVar


class Style:
    def __init__(self, root):
        self.root = root

        self.LOOP = IntVar()
        self.LOOP.set(int(1))
        self.GET_LOOP = lambda: self.LOOP.get()
        
        self.DELAY = IntVar()
        self.DELAY.set(int(5))
        self.GET_DELAY = lambda: self.DELAY.get()
        
        self.__RTEXT = StringVar()
        self.SET_RTEXT = lambda v: self.__RTEXT.set(' 录制模块: ' + v + ' ')

        self.__PTEXT = StringVar()
        self.SET_PTEXT = lambda v: self.__PTEXT.set(v)
        self.SET_PTEXT('空 闲')

    def RECORD_COMP(self, run_callback, stop_callback):

        self.SET_RTEXT('无操作')
        label = Label(self.root, textvariable=self.__RTEXT,
                      font=('宋体', 10, 'bold'),)

        record = LabelFrame(self.root, padx=10, pady=20, labelwidget=label)

        s_btn = self.__NEWBTN(record, '执 行', run_callback)
        e_btn = self.__NEWBTN(record, '停 止', stop_callback)

        s_btn.grid(column=0, row=0)
        e_btn.grid(column=1, row=0, padx=(20, 0))
        record.pack(pady=(20, 0))

    def PLAY_COMP(self, run_callback, stop_callback):

        play = LabelFrame(self.root, padx=10, pady=20,
                          text=' 播放模块: ', font=('宋体', 10, 'bold'))

        loopt = LabelFrame(play, padx=6, pady=10, text=' 循环 ',
                           font=('宋体', 10, 'bold'), labelanchor='n')
        loopt.grid(column=0, row=0, sticky='w')

        loop = Entry(loopt, width=10, textvariable=self.LOOP)
        loop.pack()

        delayt = LabelFrame(play, padx=6, pady=10, text=' 延迟 ',
                            font=('宋体', 10, 'bold'), labelanchor='n')
        delayt.grid(column=1, row=0, sticky='e')

        delay = Entry(delayt, width=10, textvariable=self.DELAY)
        delay.pack()

        start = self.__NEWBTN(play, '执 行', run_callback)
        start.grid(column=0, row=1, pady=10)

        end = self.__NEWBTN(play, '停 止', stop_callback)
        end.grid(column=1, row=1, padx=(20, 0))

        board = Label(play, textvariable=self.__PTEXT, relief=RAISED,
                      width=6, height=2, bg='#ccc', foreground='red', font=('宋体', 42, 'bold'))
        board.grid(column=0, row=2, pady=(20, 0), columnspan=2)

        play.pack(pady=(20, 0))

    def __NEWBTN(self, root, text, callback):
        button = Button(root)
        button['text'] = text
        button['width'] = 10
        button['height'] = 2
        button['font'] = ('宋体', 10, 'bold')
        button['command'] = callback
        return button
