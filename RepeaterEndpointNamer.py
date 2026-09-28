# -*- coding: utf-8 -*-
from burp import IBurpExtender
from burp import IContextMenuFactory
from burp import IExtensionStateListener
from javax.swing import JMenuItem
import java.util.ArrayList as ArrayList
import threading
import os
import time

class BurpExtender(IBurpExtender, IContextMenuFactory, IExtensionStateListener):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("Endpoint Namer (Smart Shortcut)")
        
        self.latest_messages = []
        self.running = True
        
        callbacks.registerContextMenuFactory(self)
        callbacks.registerExtensionStateListener(self)
        
        t = threading.Thread(target=self.watch_file)
        t.daemon = True
        t.start()

    def extensionUnloaded(self):
        self.running = False

    def createMenuItems(self, invocation):
        self.latest_messages = invocation.getSelectedMessages()
        
        menuList = ArrayList()
        menuItem = JMenuItem("z - Send to Repeater (Endpoint)", actionPerformed=self.menu_clicked)
        menuList.add(menuItem)
        return menuList

    def menu_clicked(self, event):
        self.send_to_repeater()

    def watch_file(self):
        trigger_file = "/tmp/burp_trigger_repeater"
        while self.running:
            if os.path.exists(trigger_file):
                try:
                    os.remove(trigger_file)
                    self.send_to_repeater()
                except:
                    pass
            time.sleep(0.01)

    def send_to_repeater(self):
        if not self.latest_messages:
            return

        for message in self.latest_messages:
            httpService = message.getHttpService()
            if not httpService:
                continue
                
            requestInfo = self._helpers.analyzeRequest(httpService, message.getRequest())
            url = requestInfo.getUrl()
            
            if not url:
                continue
                
            path = url.getPath()
            
            if not path or path == "/":
                tab_name = "Root"
            else:
                parts = [p for p in path.split('/') if p]
                if parts:
                    endpoint_name = parts[-1]
                    tab_name = endpoint_name[-15:] 
                else:
                    tab_name = "Root"
                
            self._callbacks.sendToRepeater(
                httpService.getHost(),
                httpService.getPort(),
                httpService.getProtocol() == "https",
                message.getRequest(),
                tab_name
            )