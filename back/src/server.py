from flask import Flask, request, Response, jsonify
import os
import threading
from robot_status import RobotStatus
import time

class App:
    def __init__(self) -> None:
        self.app = Flask("myApp")
        self.back_dir_name =  os.path.dirname(os.path.dirname(__file__))
        self.timer = threading.Timer(10, self.update_status)
        self.timer.start()
        self.timeout_sec = 10
        self.last_online = time.time()
        

        @self.app.route("/", methods = ['GET'])
        def index():
            index = open("{}/html/index.html".format(self.back_dir_name))
            return index
        


        @self.app.route("/js/index.js", methods =[ 'GET'])
        def js():
            js_file = open("{}/js/index.js".format(self.back_dir_name))
            return js_file       




        @self.app.route("/send_data", methods =['POST'])
        def req_data():
            if RobotStatus.key == request.json['key']:
                RobotStatus.online                      = True
                RobotStatus.uptime                      =   request.json["uptime"                      ]
                RobotStatus.ros_control_loop_freq       =   request.json["ros_control_loop_freq"       ]
                RobotStatus.mcu_and_user_port_current   =   request.json["mcu_and_user_port_current"   ]
                RobotStatus.left_driver_current         =   request.json["left_driver_current"         ]
                RobotStatus.right_driver_current        =   request.json["right_driver_current"        ]
                RobotStatus.battery_voltage             =   request.json["battery_voltage"             ]
                RobotStatus.left_driver_voltage         =   request.json["left_driver_voltage"         ]
                RobotStatus.right_driver_voltage        =   request.json["right_driver_voltage"        ]
                RobotStatus.left_driver_temp            =   request.json["left_driver_temp"            ]
                RobotStatus.right_driver_temp           =   request.json["right_driver_temp"           ]
                RobotStatus.left_motor_temp             =   request.json["left_motor_temp"             ]
                RobotStatus.right_motor_temp            =   request.json["right_motor_temp"            ]
                RobotStatus.capacity_estimate           =   request.json["capacity_estimate"           ]
                RobotStatus.charge_estimate             =   request.json["charge_estimate"             ]
                RobotStatus.timeout                     =   request.json["timeout"                     ]
                RobotStatus.lockout                     =   request.json["lockout"                     ]
                RobotStatus.e_stop                      =   request.json["e_stop"                      ]
                RobotStatus.ros_pause                   =   request.json["ros_pause"                   ]
                RobotStatus.no_battery                  =   request.json["no_battery"                  ]
                RobotStatus.current_limit               =   request.json["current_limit"               ]
                RobotStatus.last_online                 =   time.time()
                return Response(status=200)
            return Response(status=404)


       

        @self.app.route("/get_data", methods = ["GET"])
        def get_data():
            json = {
              "online"                      : RobotStatus.online                      ,
              "uptime"                      : RobotStatus.uptime                      ,
              "ros_control_loop_freq"       : RobotStatus.ros_control_loop_freq       ,
              "mcu_and_user_port_current"   : RobotStatus.mcu_and_user_port_current   ,
              "left_driver_current"         : RobotStatus.left_driver_current         ,
              "right_driver_current"        : RobotStatus.right_driver_current        ,
              "battery_voltage"             : RobotStatus.battery_voltage             ,
              "left_driver_voltage"         : RobotStatus.left_driver_voltage         ,
              "right_driver_voltage"        : RobotStatus.right_driver_voltage        ,
              "left_driver_temp"            : RobotStatus.left_driver_temp            ,
              "right_driver_temp"           : RobotStatus.right_driver_temp           ,
              "left_motor_temp"             : RobotStatus.left_motor_temp             ,
              "right_motor_temp"            : RobotStatus.right_motor_temp            ,
              "capacity_estimate"           : RobotStatus.capacity_estimate           ,
              "charge_estimate"             : RobotStatus.charge_estimate             ,
              "timeout"                     : RobotStatus.timeout                     ,
              "lockout"                     : RobotStatus.lockout                     ,
              "e_stop"                      : RobotStatus.e_stop                      ,
              "ros_pause"                   : RobotStatus.ros_pause                   ,
              "no_battery"                  : RobotStatus.no_battery                  ,
              "current_limit"               : RobotStatus.current_limit               
            }
            return  jsonify(json)


    def run(self):
        self.app.run()

    def update_status(self):
        self.timer = threading.Timer(10, self.update_status)
        self.timer.start()
        if time.time() - self.last_online > self.timeout_sec:
            RobotStatus.online = False

    

if __name__ == "__main__":
    app = App()
    app.run()
    