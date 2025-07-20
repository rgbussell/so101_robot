#!/bin/env python

from lerobot.robots.so101_follower import SO101Follower, SO101FollowerConfig

class SetupMotors:
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

        follower = SO101Follower(config)
        follower.setup_motors()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Motor asetup SO101 robot')
    parser.add_argument('--id', type=str, help='Device ID', required=True)
    args = parser.parse_args()

    calibrate = SetupMotors(args.id)
    calibrate.run()
