#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
下面这个是一个有趣的例子，主要使用了deque的rotate方法来实现了一个无限循环的加载动画
'''

import sys
import time
from collections import deque

fancy_loading = deque('>--------------------')
i = 0

while True:
    print '\r%s' % ''.join(fancy_loading),
    fancy_loading.rotate(1)
    sys.stdout.flush()
    time.sleep(0.08)
    if i >100:
        break
    i += 1

# Result:
# 一个无尽循环的跑马灯
