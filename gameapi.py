import requests
import json
import utils

class GameApi:
    baseurl = "https://ponypanic.io/playGameApi/v1/"
    def __init__(self, player_token, playthrough_token = None) -> None:
        self.player_token = player_token
        if playthrough_token is None:
            print("Creating new playthrough")
            begin_resp = self.begin_story()
            print(json.dumps(begin_resp, indent=4))
            self.playthrough_token = begin_resp["storyPlaythroughToken"]
        else:
            self.playthrough_token = playthrough_token
    
    def begin_story(self):
        url = self.baseurl + "story/begin"
        headers = {}
        headers["player-token"] = self.player_token
        resp = requests.post(url, headers=headers, timeout=5)
        return resp.json()
    
    def get_map_state(self):
        url = self.baseurl + "play/mapState"
        headers = {}
        headers["Content-Type"] = "application/json"
        headers["story-playthrough-token"] = self.playthrough_token
        resp = requests.get(url, headers=headers, timeout=5)
        return resp.json()
    
    def get_map_resource(self):
        url = self.baseurl + "play/mapResource"
        headers = {}
        headers["Content-Type"] = "application/json"
        headers["story-playthrough-token"] = self.playthrough_token
        resp = requests.get(url, headers=headers, timeout=5)
        return resp.json()