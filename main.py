import gameapi
import utils
from map import Map, MapEntity
from tokens import player_token, playthrough_token

api = gameapi.GameApi(player_token, playthrough_token)

mapstate = api.get_map_state()
mapres = api.get_map_resource()
print(f"{mapres=}")
print(f"{mapstate=}")
map = Map(mapstate, mapres)
print(map)