#!/usr/bin/env python
import argparse
import dbus
import sys

def run_command(args):
    """Runs the specified command."""
    bus = dbus.SessionBus()
    proxy_object = bus.get_object('org.gnome.ScreenSaver', '/org/gnome/ScreenSaver')
    screensaver = dbus.Interface(proxy_object, dbus_interface='org.gnome.ScreenSaver')
    if args.command == 'lock':
        print 'Locking the screen...'
        screensaver.Lock()
    else:
        print 'Unlocking the screen...'
        screensaver.SetActive(dbus.Boolean(0))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Controls the lock screen')
    parser.add_argument('command',
                        metavar='COMMAND',
                        type=str,
                        choices=['lock', 'unlock'],
                        help='either "lock" or "unlock"')
    run_command(parser.parse_args())
