from sys import exit
import PySimpleGUI as psg
from core import SuperWorkerBee
from conf.interface import element

psg.theme('Default1')
layout = element()  # todo 样式
window = psg.Window('SuperWorkerBee', layout,
                    icon='favicon.ico', size=(400, 400))


if __name__ == '__main__':

    swb = SuperWorkerBee(psg, window)

    while True:  # todo 事件循环并获取输入值

        event, values = window.read()

        if event == psg.WIN_CLOSED:  # todo 关闭程序
            window.close()
            exit()

        if event == "-RECORDBTN-":  # todo 录制
            swb.recordStart(values)

        if event == '-RECORDSTOP-':  # todo 停止录制
            swb.recordStop()

        if event == "-PLAYBTN-":  # todo 播放
            swb.executeStart(values)

        if event == '-PLAYSTOP-':  # todo 停止播放
            swb.executeStop()

        if event == "-FEILDEL-":  # todo 删除单个文件
            swb.delFile(values)

        if event == '-RESET-':  # todo 删除全部文件
            swb.resetFile()

window.close()
