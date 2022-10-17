# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node
from pynmeagps import NMEAReader
# import serial

# from std_msgs.msg import String
from sensor_msgs.msg import NavSatFix

# for serial read
# ser = serial.Serial('/dev/ttyACM0', 9600)

# for reading through a file
def readFile(file):
    f = open(file, "r")
    # Read line by line.
    for line in f:
        pass
    return line

# change to the correct path
filePath = "/home/ching/GNSS/data/edited_GNSS_data.txt"

class GNSSpublisher(Node):

    def __init__(self):
        super().__init__('gnss_publisher')
        self.gnss_publisher_= self.create_publisher(NavSatFix, 'nmeagns_message', 10)
        timer_period = 0.5 # 0.5 seconds
        self.gnss_timer_= self.create_timer(timer_period, self.publish_gnss)
        self.i = 0

    def publish_gnss(self):
        # nmeagns_message = NMEAReader.parse("$GNGNS,103600.01,5114.51176,N,00012.29380,W,ANNN,07,1.18,111.5,45.6,,,V*00")
        # nmeagns_message = NMEAReader.parse(ser.readline())
        
        # change file name to actual file
        nmeagns_message = NMEAReader.parse(readFile(filePath))
        gnss_msg = NavSatFix()
        UTC_time = nmeagns_message.time.strftime("%X")
        # gnss_msg.header.stamp = nmeagns_message.time
        t = self.get_clock().now()
        gnss_msg.header.stamp = t.to_msg()
        gnss_msg.header.frame_id = "gnss"
        gnss_msg.latitude = float(nmeagns_message.lat)
        gnss_msg.longitude = float(nmeagns_message.lon)
        gnss_msg.altitude = float(nmeagns_message.alt)
        self.gnss_publisher_.publish(gnss_msg)
        self.get_logger().info('Publishing: data %d, time = %s, long =  %f, lat = %f, alt = %f' % (self.i, UTC_time, gnss_msg.longitude, gnss_msg.latitude, gnss_msg.altitude))
        self.i += 1


def main(args=None):
    rclpy.init(args=args)
    # define node
    gnss_publisher = GNSSpublisher()
    rclpy.spin(gnss_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    gnss_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
