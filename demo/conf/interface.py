
import PySimpleGUI as sg
from conf.utils import getFileList, createdFile

createdFile('json')
file_list = getFileList('json')


def element():
    # todo 录制模块
    record = [sg.T('*录制文件名称:'),
              sg.In(key='-RECORD-', size=(16, 1)),
              sg.B('录制', key='-RECORDBTN-', size=(6, 2)),
              sg.B('停止', key='-RECORDSTOP-', pad=((20, 10), (20, 20)), size=(6, 2))]
    recordFrame = [sg.Frame(" 录制功能 ", [record], pad=((2, 0), (20, 10)))]

    # todo 播放选择模块
    playConf = [sg.T('*选择播放文件:'),
                sg.Combo(file_list, key='-PLAY-',
                         size=(15, 1),  readonly=True),
                sg.B('删除', key='-FEILDEL-', size=(6, 2)),
                sg.B('重置', key='-RESET-', pad=((10, 10), (8, 8)), size=(6, 2))]
    # todo 播放模块
    play = [sg.T('循环次数: '),
            sg.In(1, key='-NUM-', size=(6, None)),
            sg.T('延迟 / s:'),
            sg.In(3, key='-DELAY-', size=(4, None)),
            sg.B('播放', key='-PLAYBTN-', size=(6, 2)),
            sg.B('停止', key='-PLAYSTOP-', pad=((10, 10), (15, 15)), size=(6, 2))]
    playFrame = [sg.Frame(" 播放功能 ", [playConf, play], pad=((2, 0), (10, 10)))]

    # todo 功能说明
    toolList = [sg.T('状态:', ),
                sg.In('空闲', key='-INDEX-', size=(10, None),
                      text_color='#FF0018', disabled=True, justification='center'), sg.T('停止录制 / delete', pad=((20, 10), (10, 10)))]
    toolFrame = [sg.Frame(" 其他 ", [toolList], pad=((2, 0), (10, 10)))]

    return [recordFrame, playFrame, toolFrame]
