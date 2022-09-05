#!/usr/bin/env python3
import rospy
import requests
from husky_msgs.msg import HuskyStatus
import subprocess
import json
class Client:
    def __init__(self, url) -> None:
        self.url = url + "/send_data"
        self.sub = rospy.Subscriber("/status", HuskyStatus, callback=self.callback)
    


    def callback(self, status : HuskyStatus):
        
        data = {
                "key" : "12312321",
              "uptime"                      : status.uptime                             ,
              "ros_control_loop_freq"       : status.ros_control_loop_freq              ,
              "mcu_and_user_port_current"   : status.mcu_and_user_port_current          ,
              "left_driver_current"         : status.left_driver_current                ,
              "right_driver_current"        : status.right_driver_current               ,
              "battery_voltage"             : status.battery_voltage                    ,
              "left_driver_voltage"         : status.left_driver_voltage                ,
              "right_driver_voltage"        : status.right_driver_voltage               ,
              "left_driver_temp"            : status.left_driver_temp                   ,
              "right_driver_temp"           : status.right_driver_temp                  ,
              "left_motor_temp"             : status.left_motor_temp                    ,
              "right_motor_temp"            : status.right_motor_temp                   ,
              "capacity_estimate"           : status.capacity_estimate                  ,
              "charge_estimate"             : status.charge_estimate                    ,
              "timeout"                     : status.timeout                            ,
              "lockout"                     : status.lockout                            ,
              "e_stop"                      : status.e_stop                             ,
              "ros_pause"                   : status.ros_pause                          ,
              "no_battery"                  : status.no_battery                         ,
              "current_limit"               : status.current_limit               
            }
        requests.post(self.url, json=data)


def main():
    rospy.init_node("cliet_status_sender")
    bashCommand = "ngrok api  tunnels list --api-key $NGROK_API_KEY"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    json_obj = json.loads(output)
    url = json_obj['tunnels'][0]['public_url']
    o = Client(url)
    
    rospy.spin()

if __name__ == "__main__":
    main()