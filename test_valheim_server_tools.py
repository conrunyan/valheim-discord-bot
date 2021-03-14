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

from testing_resources import log_data
from valheim_server_tools import get_login_events


class TestGetActivePlayers:
    pass


class TestGetLoginEvents:
    def test_get_login_events_no_zoids(self, log_data):
        expected = {
            "692335600": {
                "username": "Lars",
                "timestamp": "03/14/2021 07:14:33",
                "action": "LOG_IN",
            },
            "561945071": {
                "username": "Lars",
                "timestamp": "03/14/2021 07:17:25",
                "action": "LOG_IN",
            },
            "1555652395": {
                "username": "Bubbert",
                "timestamp": "03/14/2021 07:21:40",
                "action": "LOG_IN",
            },
        }
        result = get_login_events(log_data)
        assert expected == result


class TestGetLogoutEvents:
    pass