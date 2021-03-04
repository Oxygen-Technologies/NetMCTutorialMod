# -*- coding: utf-8 -*-
from mod.common.mod import Mod
import mod.server.extraServerApi as serverApi


@Mod.Binding(name='NetMCTutorialMod', version='0.0.1')
class NetMCTutorialMod(object):
    @Mod.InitServer()
    def server_init(self):
        serverApi.RegisterSystem('NetMCTutorialMod', 'TutorialServerSystem',
                                 'tutorial_scripts.server_system.TutorialServerSystem')
