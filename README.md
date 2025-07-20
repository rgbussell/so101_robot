# so101_robot
Experiments with so101_robot

# Setup
* 2 robot arms -- follower

# calibration file
~/.cache/huggingface/lerobot/calibration
-> robots
-> teleoperators
-->so101_leader/leader_arm.json

# usb calibration
configs/usb.json # reading the updated usb ports from this file

# Command reference (lerobot environment)

# Detect a connected camera
python -m lerobot.find_cameras opencv

# teleoperate
python -m lerobot.teleoperate
--robot.type=so101_follower
--robot.port=/dev/tty.usbmodem5A680085401
--robot.id=my_follower_arm
--teleop.type=so101_leader
--teleop.port=/dev/tty.usbmodem5A680109561
--teleop.id=leader_arm

For some reason the teleoperator.py script does not work 
as it cannot find lerobot.common. Maybe an install issue
instead we just use the command line setup