# -*- coding: utf-8 -*-
from .netmc import Mod
from .netmc.server import ServerSystemBase
from .netmc.server.event import ServerChatEvent
from .netmc.server.behavior import ItemData


@Mod.system
class TutorialServerSystem(ServerSystemBase):
    def __init__(self, namespace, system_name):
        super(TutorialServerSystem, self).__init__(namespace, system_name)

    @ServerChatEvent.callback
    def on_chat(self, event):
        # type: (ServerChatEvent) -> None
        item_name = {
            '钻石剑': 'minecraft:diamond_sword',
            '钻石稿': 'minecraft:diamond_pickaxe',
            '钻石头盔': 'minecraft:diamond_helmet',
            '钻石胸甲': 'minecraft:diamond_chestplate',
            '钻石护腿': 'minecraft:diamond_leggings',
            '钻石靴子': 'minecraft:diamond_boots',
        }.get(event.message)

        if item_name:
            event.player.spawn_item_to_inventory(ItemData(item_name, 1, 0))
