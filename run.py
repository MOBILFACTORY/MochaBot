#!/usr/bin/python
# -*- coding: utf-8 -*-

from hipchatAPI import HipchatAPI
import datetime, time

#914267 - Project N
#896106 - MobilFactory

hc = HipchatAPI('HIPCHAT_ACCESS_KEY')
#hc.message('914267', 'Mocha Bot', 'Test')

MF_ROOM_ID = '896106'
PN_ROOM_ID = '914267'

# TODO: webo 새글 알림.

timeEvents = [
    #(roomId(str), weekdayOnly(bool), hour(int), minute(int), message(str), useHTML(bool))
    #(MF_ROOM_ID, True, 12,59,u'<p><strong>Blond</strong>: 여러분 식사하세요</p><br/><img src="https://lh5.googleusercontent.com/-PjQzpY4hf-8/VE-zf51Cw_I/AAAAAAAAVW0/hUPVOb6ne6U/s170-no/3e0e33321bf487cd9ffbf382340ae1b2.gif">', True),
    (MF_ROOM_ID, True, 12,59,u'<p><strong>Blond</strong>: 여러분 식사하세요</p>', True),
    (PN_ROOM_ID, True, 16,00,u'노리가 배고픈 4시를 알려드립니다.', False),
]


BIRTH_MSG = u'<p><strong>%s</strong> 생일 축하합니당!</p><br/><img src="https://lh5.googleusercontent.com/-k46rY2tGNGg/VFBAISLVexI/AAAAAAAAVXc/Z3pnOtfbkgc/w400-h300-no/freeboard-100617174415.gif">'
birthEvents = [
    #(roomId(str), month(int), day(int), message(str), useHTML(bool))
    (MF_ROOM_ID, 6, 25, BIRTH_MSG % (u'세림'), True),
    (MF_ROOM_ID, 9, 30, BIRTH_MSG % (u'노리'), True),
    (MF_ROOM_ID, 12, 22, BIRTH_MSG % (u'갱플'), True),
    (MF_ROOM_ID, 10, 29, BIRTH_MSG % (u'데이빗'), True),
]

lastH, lastM = -1, -1

while(True):
    curdt = datetime.datetime.now()
    weekday = curdt.weekday()
    curtime = curdt.time()

    #print 'Test %d:%d:%d' % (curtime.hour, curtime.minute, curtime.second)
    if lastH == curtime.hour and lastM == curtime.minute:
        time.sleep(30)
        continue

    # monday ~ friday
    isWeekday = (weekday >= 0 and weekday <= 4)

    for birthEvent in birthEvents:
        if birthEvent[1] == curdt.month and birthEvent[2] == curdt.day:
            if curtime.hour == 10 and curtime.minute == 0:
                hc.message(birthEvent[0], 'Mocha Bot', birthEvent[3], 'html' if timeEvent[4] else 'text')

    for timeEvent in timeEvents:
        if timeEvent[1] and not isWeekday:
            continue

        if timeEvent[2] == curtime.hour and timeEvent[3] == curtime.minute:
            hc.message(timeEvent[0], 'Mocha Bot', timeEvent[4], 'html' if timeEvent[5] else 'text')

    lastH, lastM = curtime.hour, curtime.minute

    #hc.message(timeEvent[0], 'Mocha Bot', 'Test %d:%d:%d' % (curtime.hour, curtime.minute, curtime.second))
    time.sleep(30)

#import code
#code.interact(local=locals())
