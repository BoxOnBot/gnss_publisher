# gnss_publisher
A simple ROS2 publisher in Python to take in serial data and publish LLH using NavSatFix messages

## Serial input (Optional)
/dev/ttyACM0

## Read from file (Optional)
Reads from a file (reads the last line), however the path and file name must be edited first

## Input type
NMEA GNS message type

*Example*: $GNGNS,103600.01,5114.51176,N,00012.29380,W,ANNN,07,1.18,111.5,45.6,,,V*00

## Output topic message type
NMEA message parsed using [pynmeagps module](https://pypi.org/project/pynmeagps/)

[NavSatFix](http://docs.ros.org/en/melodic/api/sensor_msgs/html/msg/NavSatFix.html) message with latitude, longitude and altitude
