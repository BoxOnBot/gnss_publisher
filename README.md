# gnss_publisher
A simple ROS2 publisher in Python to take in serial data and publish LLH using NavSatFix messages

## Serial input
/dev/ttyACM0

## Input type
NMEA GNS message type

*Example*: $GNGNS,103600.01,5114.51176,N,00012.29380,W,ANNN,07,1.18,111.5,45.6,,,V*00

### Publisher output topic
NavSatFix message with latitude, longitude and altitude
