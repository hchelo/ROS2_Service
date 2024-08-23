# ROS 2 Service Practice

Turn on an LED on an ESP32 from a laptop1 server and a laptop2 client

Configuration Diagram:

![Configuration Diagram](https://github.com/hchelo/ROS2_basics/blob/main/img/ROS2%20Esp32%20led.png)

# 0. In the ESP32 
sudo chmod 777 /dev/ttyUSB0 
Upload the following program to the ESP32. Don't forget to connect the ESP32 to the same Wi-Fi network as your PCs.
- esp_led.py

Afterward, you can disconnect the ESP32 and test it with a separate 5V power supply.

# 1. Create new package
Open a new terminal and source, in this case: esp32_ws/src/

create:
- ros2 pkg create --build-type ament_python py_srvcli --dependencies rclpy example_interfaces

# 2 Write the service node

- serviesp.py

# 3 Write the client node

- cliesp.py

# 4 Build and run
- colcon build
- source install/setup.bash

SERVER:
	ros2 run py_srvcliESP minimal_service 

CLIENT
	ros2 run py_srvcliESP minimal_client 1

If the argument is 1, it turns on the LED on the ESP32; if the argument is 0, the LED turns off.

