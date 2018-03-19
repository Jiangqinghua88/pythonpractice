#! /usr/bin/env python
# -*- coding: utf-8 -*-

import struct
import _winreg
import sys

#proxy = sys.argv[1]
proxy = "proxy.ericsson.se:8080"
root = _winreg.HKEY_CURRENT_USER
proxy_path = r"Software\Microsoft\Windows\CurrentVersion\Internet Settings"
kv_Enable = [
  (proxy_path, "ProxyEnable", 1, _winreg.REG_DWORD),
  #(proxy_path, "ProxyServer", 1, _winreg.REG_DWORD),
]

kv_Disable = [
  (proxy_path, "ProxyEnable", 0, _winreg.REG_DWORD),
  #(proxy_path, "ProxyServer", 0, _winreg.REG_DWORD),
]

hKey = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, proxy_path)
value, type = _winreg.QueryValueEx(hKey, "ProxyEnable")
kv = kv_Enable
result = "Enabled"
if value:
    result = "Disabled"
    kv = kv_Disable


for keypath, value_name, value, value_type in kv:
    hKey = _winreg.CreateKey (root, keypath)
    _winreg.SetValueEx (hKey, value_name, 0, value_type, value)

print result