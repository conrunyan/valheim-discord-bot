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

from testing_resources import log_data, log_data_no_zoids
from valheim_server_tools import (
    get_player_events,
    PlayerAction,
    get_active_players,
    format_active_player_message,
)


class TestGetActivePlayers:
    def test_get_active_players_one_logged_in(self):
        log_path = "./resources/sample_log.txt"
        expected = {
            "123456789": {
                "username": "Velma",
                "timestamp": "03/14/2021 08:00:26",
                "action": "ONLINE",
            },
        }
        result = get_active_players(log_path)
        assert expected == result

    def test_format_active_player_message(self):
        log_path = "./resources/sample_log.txt"
        expected = "Name, Logged-in:\nVelma,03/14/2021 08:00:26 UTC"
        active_players = get_active_players(log_path)
        result = format_active_player_message(active_players)
        assert expected == result


class TestGetLoginEvents:
    def test_get_login_events_with_valid_zdoids(self, log_data):
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
        result = get_player_events(log_data, action_type=PlayerAction.LOG_IN)
        assert expected == result

    def test_get_login_events_no_zdoids(self, log_data_no_zoids):
        expected = {}
        result = get_player_events(log_data_no_zoids, action_type=PlayerAction.LOG_IN)
        assert expected == result

    def test_get_player_events_invalid_action_type(self):
        with pytest.raises(ValueError):
            get_player_events("", "TOTALY REAL EVENT TYPE")


class TestGetLogoutEvents:
    def test_get_logout_events(self, log_data):
        expected = {
            "692335600": {
                "username": "",
                "timestamp": "03/14/2021 07:15:02",
                "action": "LOG_OUT",
            },
            "561945071": {
                "username": "",
                "timestamp": "03/14/2021 07:17:37",
                "action": "LOG_OUT",
            },
            "1555652395": {
                "username": "",
                "timestamp": "03/14/2021 11:47:52",
                "action": "LOG_OUT",
            },
        }
        result = get_player_events(log_data, action_type=PlayerAction.LOG_OUT)
        assert expected == result