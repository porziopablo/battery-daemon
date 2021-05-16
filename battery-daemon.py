#!/usr/bin/env python
 
import sys, time
import dbus
from daemon import Daemon
 
class BatteryDaemon(Daemon):
 """ Daemon that checks battery percentage and state using info
 provided by `D-BUS`, and logs when the battery is full and connected to AC. """

 def checkBattery(self):
  # connects to system bus daemon       
  bus = dbus.SystemBus()

  # gets proxy object that connects to app providing battery info through an interface
  batteryObject = bus.get_object('org.freedesktop.UPower', '/org/freedesktop/UPower/devices/battery_BAT0')
  battery = dbus.Interface(batteryObject, 'org.freedesktop.DBus.Properties')

  # gets battery percentage and state
  batteryPercentage = battery.Get("org.freedesktop.UPower.Device", "Percentage")
  batteryState = battery.Get("org.freedesktop.UPower.Device", "State")

 def run(self):
  while True:
   self.checkBattery()
   time.sleep(1)

def main():
 daemon = BatteryDaemon('/tmp/battery-daemon.pid')
 if len(sys.argv) == 2:
  if 'start' == sys.argv[1]:
   daemon.start()
  elif 'stop' == sys.argv[1]:
   daemon.stop()
  elif 'restart' == sys.argv[1]:
   daemon.restart()
  else:
   print("Unknown command")
   sys.exit(2)
 sys.exit(0)
