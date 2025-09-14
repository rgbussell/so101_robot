python -m lerobot.record \
    --robot.type=so101_follower \
    --robot.port=/dev/tty.usbmodem5A680085401 \
    --robot.id=my_follower_arm \
    --robot.cameras="{ front: {type: opencv, index_or_path: 0, width: 1920, height: 1080, fps: 30}}" \
    --teleop.type=so101_leader \
    --teleop.port=/dev/tty.usbmodem5A680109561 \
    --teleop.id=leader_arm \
    --display_data=true \
    --dataset.repo_id=${HF_USER}/record-test \
    --dataset.num_episodes=5 \
    --dataset.single_task="Grab the black tray" \
    --dataset.episode_time_s=15 \
    --dataset.reset_time=5

# replay a training episode
python -m lerobot.replay \
  --robot.type=so101_follower \
  --robot.port=/dev/tty.usbmodem5A680085401 \
  --robot.id=my_follower_arm \
  --dataset.repo_id=${HF_USER}/record-test \
  --dataset.episode=0

# train the model
python -m lerobot.scripts.train \
  --dataset.repo_id=${HF_USER}/record-test \
  --policy.type=act \
  --output_dir=outputs/train/act_record_test \
  --job_name=act_record_test \
  --policy.device=mps \
  --wandb.enable=true \
  --policy.repo_id=${HF_USER}/my_policy
