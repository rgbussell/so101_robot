from lerobot.common.teleoperators.so101_leader import SO101LeaderConfig, SO101Leader
from lerobot.common.robots.so101_follower import SO101FollowerConfig, SO101Follower

with open("../config/usb.json") as f:
    usb_config = json.load(f)

id = "follower_arm"
robot_config = SO101FollowerConfig(
    port=usb_config[id]["port"],
    id=id,
)

id = "leader_arm"
teleop_config = SO101LeaderConfig(
    port=usb_config[id]["port"],
    id=id,
)

robot = SO101Follower(robot_config)
teleop_device = SO101Leader(teleop_config)
robot.connect()
teleop_device.connect()

while True:
    action = teleop_device.get_action()
    robot.send_action(action)
