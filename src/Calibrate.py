#!/bin/env python

from lerobot.robots.so101_follower import SO101FollowerConfig, SO101Follower
import json
import argparse

class Calibrate:
    def __init__(self, id):
        with open("../config/usb.json") as f:
            usb_config = json.load(f)

        try:
            config = usb_config[id]
        except:
            raise ValueError(f"USB configuration for ID {id} not found in usb.json")    

        config = SO101FollowerConfig(
            port=config["port"],
            id=id,
        )

        self.follower = SO101Follower(config)
        
    def run(self):
        self.follower.connect(calibrate=False)
        self.follower.calibrate()
        self.follower.disconnect()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calibrate SO101 robot')
    parser.add_argument('--id', type=str, help='Device ID', required=True)
    args = parser.parse_args()

    calibrate = Calibrate(args.id)
    calibrate.run()


