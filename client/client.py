#!/usr/bin/env python3
import rospy
import requests
from husky_msgs.msg import HuskyStatus

class Client:
    def __init__(self) -> None:
        self.url = "https://eced-93-175-20-92.eu.ngrok.io/send_data"
        self.sub = rospy.Subscriber("/status", HuskyStatus, callback=self.callback)
    


    def callback(self, status : HuskyStatus):
        
        data = {
              "key" : "12312321",
              "uptime"                      : status.uptime                      ,
              "ros_control_loop_freq"       : status.ros_control_loop_freq       ,
              "mcu_and_user_port_current"   : status.mcu_and_user_port_current   ,
              "left_driver_current"         : status.left_driver_current         ,
              "right_driver_current"        : status.right_driver_current        ,
              "battery_voltage"             : status.battery_voltage             ,
              "left_driver_voltage"         : status.left_driver_voltage         ,
              "right_driver_voltage"        : status.right_driver_voltage        ,
              "left_driver_temp"            : status.left_driver_temp            ,
              "right_driver_temp"           : status.right_driver_temp           ,
              "left_motor_temp"             : status.left_motor_temp             ,
              "right_motor_temp"            : status.right_motor_temp            ,
              "capacity_estimate"           : status.capacity_estimate           ,
              "charge_estimate"             : status.charge_estimate             ,
              "timeout"                     : status.timeout                     ,
              "lockout"                     : status.lockout                     ,
              "e_stop"                      : status.e_stop                      ,
              "ros_pause"                   : status.ros_pause                   ,
              "no_battery"                  : status.no_battery                  ,
              "current_limit"               : status.current_limit               
            }
        requests.post(self.url, json=data)


def main():
    rospy.init_node("cliet_status_sender")
    o = Client()
    rospy.spin()

if __name__ == "__main__":
    main()