#!/usr/bin/env python3
from os import path, makedirs
from tkinter import Tk
from core import Interface


class GUI:
    'worker bee entrance'

    def __init__(self):
        self.root = Tk()
        self.root.title("Worker Bee")
        self.root.iconbitmap("favicon.ico")
        self.root.geometry("240x450")
        self.setup(self.root)

    def setup(self, root):

        # todo 创建资源文件夹
        if not path.exists('assets'):
            makedirs('assets')

        # todo 渲染Gui界面
        Interface(root)


if __name__ == '__main__':
    app = GUI()
    app.root.resizable(False, False)
    app.root.mainloop()
