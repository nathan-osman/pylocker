#!/usr/bin/env python3
import sys
import dbus

bus = dbus.SessionBus()
proxy_object = bus.get_object('org.gnome.ScreenSaver', '/org/gnome/ScreenSaver')
screensaver = dbus.Interface(proxy_object,
              dbus_interface='org.gnome.ScreenSaver')

def screenlocker(a):
    if a == 'lock':
        screensaver.Lock()
    elif a == 'unlock':
        dbusfalse = dbus.Boolean(0)
        screensaver.SetActive(dbusfalse)
    else:
        print 'Use "lock" or "unlock" to lock or unlock the screen'

if __name__ == "__main__":
    import sys
    screenlocker(sys.argv[1])
