#!/bin/env python

from lerobot.robots.so101_follower import SO101Follower, SO101FollowerConfig

config = SO101FollowerConfig(
    port="/dev/tty.usbmodem5A680109561",
    id="leader_arm",
)
follower = SO101Follower(config)
follower.setup_motors()
