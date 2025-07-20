python -m lerobot.teleoperate \
    --robot.type=so101_follower \
    --robot.port=/dev/tty.usbmodem5A680085401 \
    --robot.id=follower_arm \
    --robot.cameras="{ front: {type: opencv, index_or_path: 0, width: 1920, height: 1080, fps: 30}}" \
    --teleop.type=so101_leader \
    --teleop.port=/dev/tty.usbmodem5A680109561 \
    --teleop.id=leader_arm \
    --display_data=true
