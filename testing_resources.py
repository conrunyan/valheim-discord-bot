"""
MIT License

Copyright (c) 2021 Connor Runyan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import pytest


@pytest.fixture
def log_data():
    return """
Mar 14 07:14:13 localhost start_valheim.sh[12067]: (Filename: ./Runtime/Export/Debug/Debug.bindings.h Line: 35)
Mar 14 07:14:33 localhost start_valheim.sh[12067]: 03/14/2021 07:14:33: Got character ZDOID from Lars : 692335600:1
Mar 14 07:14:33 localhost start_valheim.sh[12067]:  
Mar 14 07:17:05 localhost start_valheim.sh[12067]: (Filename: ./Runtime/Export/Debug/Debug.bindings.h Line: 35)
Mar 14 07:17:25 localhost start_valheim.sh[12067]: 03/14/2021 07:17:25: Got character ZDOID from Lars : 561945071:1
Mar 14 07:17:25 localhost start_valheim.sh[12067]:  
Mar 14 07:21:21 localhost start_valheim.sh[12067]: (Filename: ./Runtime/Export/Debug/Debug.bindings.h Line: 35)
Mar 14 07:21:40 localhost start_valheim.sh[12067]: 03/14/2021 07:21:40: Got character ZDOID from Bubbert : 1555652395:1
Mar 14 07:21:40 localhost start_valheim.sh[12067]:  
Mar 14 07:55:01 localhost CRON[6744]: (root) CMD (command -v debian-sa1 > /dev/null && debian-sa1 1 1)
Mar 14 08:00:18 localhost start_valheim.sh[12067]: 03/14/2021 08:00:18: Got character ZDOID from Bubbert : 0:0
Mar 14 08:00:18 localhost start_valheim.sh[12067]:  
Mar 14 08:00:18 localhost start_valheim.sh[12067]: (Filename: ./Runtime/Export/Debug/Debug.bindings.h Line: 35)
Mar 14 08:00:26 localhost start_valheim.sh[12067]: 03/14/2021 08:00:26: Got character ZDOID from Bubbert : 1555652395:5036
Mar 14 08:00:26 localhost start_valheim.sh[12067]:
Mar 14 07:15:02 localhost start_valheim.sh[12067]: (Filename: ./Runtime/Export/Debug/Debug.bindings.h Line: 35)
Mar 14 07:15:02 localhost start_valheim.sh[12067]: 03/14/2021 07:15:02: Destroying abandoned non persistent zdo 692335600:1 owner 692335600
Mar 14 07:15:02 localhost start_valheim.sh[12067]:  
Mar 14 07:15:02 localhost start_valheim.sh[12067]: (Filename: ./Runtime/Export/Debug/Debug.bindings.h Line: 35)
Mar 14 07:15:02 localhost start_valheim.sh[12067]: 03/14/2021 07:15:02: Destroying abandoned non persistent zdo 692335600:12 owner 692335600
Mar 14 07:15:02 localhost start_valheim.sh[12067]:  
Mar 14 07:15:02 localhost start_valheim.sh[12067]: (Filename: ./Runtime/Export/Debug/Debug.bindings.h Line: 35)
Mar 14 07:15:02 localhost start_valheim.sh[12067]: 03/14/2021 07:15:02: Destroying abandoned non persistent zdo 692335600:13 owner 692335600
Mar 14 07:15:02 localhost start_valheim.sh[12067]:  
Mar 14 07:17:37 localhost start_valheim.sh[12067]: (Filename: ./Runtime/Export/Debug/Debug.bindings.h Line: 35)
Mar 14 07:17:37 localhost start_valheim.sh[12067]: 03/14/2021 07:17:37: Destroying abandoned non persistent zdo 561945071:1 owner 561945071
Mar 14 07:17:37 localhost start_valheim.sh[12067]:  
Mar 14 11:47:52 localhost start_valheim.sh[12067]: (Filename: ./Runtime/Export/Debug/Debug.bindings.h Line: 35)
Mar 14 11:47:52 localhost start_valheim.sh[12067]: 03/14/2021 11:47:52: Destroying abandoned non persistent zdo 1555652395:5036 owner 1555652395
Mar 14 11:47:52 localhost start_valheim.sh[12067]:  
Mar 14 11:47:52 localhost start_valheim.sh[12067]: (Filename: ./Runtime/Export/Debug/Debug.bindings.h Line: 35)
Mar 14 11:47:52 localhost start_valheim.sh[12067]: 03/14/2021 11:47:52: Destroying abandoned non persistent zdo 1555652395:40580 owner 1555652395
Mar 14 11:47:52 localhost start_valheim.sh[12067]:  
Mar 14 11:47:52 localhost start_valheim.sh[12067]: (Filename: ./Runtime/Export/Debug/Debug.bindings.h Line: 35)
Mar 14 11:47:52 localhost start_valheim.sh[12067]: 03/14/2021 11:47:52: Destroying abandoned non persistent zdo 1555652395:40578 owner 1555652395
Mar 14 11:47:52 localhost start_valheim.sh[12067]:  
Mar 14 11:47:52 localhost start_valheim.sh[12067]: (Filename: ./Runtime/Export/Debug/Debug.bindings.h Line: 35)
Mar 14 11:47:52 localhost start_valheim.sh[12067]: 03/14/2021 11:47:52: Destroying abandoned non persistent zdo 1555652395:40579 owner 1555652395
Mar 14 11:47:52 localhost start_valheim.sh[12067]:  
"""

@pytest.fixture
def log_data_no_zoids():
  return """
Mar 14 06:32:05 localhost start_valheim.sh[12067]: Total: 860.463210 ms (FindLiveObjects: 100.000560 ms CreateObjectMapping: 25.237920 ms MarkObjects: 734.115960 ms  DeleteObjects: 1.103200 ms)
Mar 14 06:35:01 localhost CRON[13810]: (root) CMD (command -v debian-sa1 > /dev/null && debian-sa1 1 1)
Mar 14 06:39:38 localhost systemd[1]: Started Session 1778 of user root.
Mar 14 06:42:04 localhost start_valheim.sh[12067]: 03/14/2021 06:42:04:  Connections 0 ZDOS:351191  sent:0 recv:0
Mar 14 06:42:04 localhost start_valheim.sh[12067]:  
Mar 14 06:42:04 localhost start_valheim.sh[12067]: (Filename: ./Runtime/Export/Debug/Debug.bindings.h Line: 35)
Mar 14 06:42:04 localhost start_valheim.sh[12067]: Unloading 0 Unused Serialized files (Serialized files now loaded: 0)
Mar 14 06:42:05 localhost start_valheim.sh[12067]: Unloading 0 unused Assets to reduce memory usage. Loaded Objects now: 1116798.
Mar 14 06:42:05 localhost start_valheim.sh[12067]: Total: 845.133610 ms (FindLiveObjects: 99.563960 ms CreateObjectMapping: 25.001810 ms MarkObjects: 719.591680 ms  DeleteObjects: 0.971310 ms)
Mar 14 06:42:06 localhost start_valheim.sh[12067]: 03/14/2021 06:42:06: clone 1004
Mar 14 06:42:06 localhost start_valheim.sh[12067]:  
Mar 14 06:42:06 localhost start_valheim.sh[12067]: (Filename: ./Runtime/Export/Debug/Debug.bindings.h Line: 35)
Mar 14 06:42:08 localhost start_valheim.sh[12067]: 03/14/2021 06:42:08: Saved 351191 zdos
Mar 14 06:42:08 localhost start_valheim.sh[12067]:  
Mar 14 06:42:08 localhost start_valheim.sh[12067]: (Filename: ./Runtime/Export/Debug/Debug.bindings.h Line: 35)
Mar 14 06:42:08 localhost start_valheim.sh[12067]: 03/14/2021 06:42:08: World saved ( 1524.962ms )
Mar 14 06:42:08 localhost start_valheim.sh[12067]:  
"""