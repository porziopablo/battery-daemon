#!/usr/bin/env python
 
import sys, time
import dbus
from daemon import Daemon
from enum import Enum

class BATTERY_POWER_STATE(Enum):
 """ Battery states provided by `freedesktop.UPower` """

 UNKNOWN = 0
 CHARGING = 1
 DISCHARGING = 2
 EMPTY = 3
 FULLY_CHARGED = 4
 PENDING_CHARGE = 5
 PENDING_DISCHARGE = 6

class AC_POWER_STATE(Enum):
 """ AC power line states provided by `freedesktop.UPower` """

 OFFLINE = 0
 ONLINE = 1

class BatteryDaemon(Daemon):
 """ Daemon that checks battery percentage and state using info
 provided by `D-BUS`, and logs when the battery is full and connected to AC power. """

 def initProxies(self):
  """ Initializes proxies that supply info about battery and AC power
  from `UPower` application through an interface. """

  # connects to system bus daemon       
  bus = dbus.SystemBus()

  # gets proxy for battery info
  batteryObject = bus.get_object('org.freedesktop.UPower', '/org/freedesktop/UPower/devices/battery_BAT0')
  batteryProxy = dbus.Interface(batteryObject, 'org.freedesktop.DBus.Properties')

  # gets proxy for AC power
  acObject = bus.get_object('org.freedesktop.UPower', '/org/freedesktop/UPower/devices/line_power_AC')
  acProxy = dbus.Interface(acObject, 'org.freedesktop.DBus.Properties')

  return [acProxy, batteryProxy]

 def isBatteryFull(self, batteryProxy):
  """ Checks if battery is fully charged. """

  batteryState = batteryProxy.Get("org.freedesktop.UPower.Device", "State")

  print(batteryState == BATTERY_POWER_STATE.FULLY_CHARGED.value)

 def isACPowerOn(self, acProxy):
  """ Checks if AC power line is connected. """

  acState = acProxy.Get('org.freedesktop.UPower.Device', 'Online')

  print(acState == AC_POWER_STATE.ONLINE.value)

 def run(self):
  [acProxy, batteryProxy] = self.initProxies()

  while True:
   self.isBatteryFull(batteryProxy)
   self.isACPowerOn(acProxy)
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

main()