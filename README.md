# JUENO
JUENO-AI: The Ultimate Video Game AI Blueprint
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>GameBot-AI Repository Structure</title>
    <style>
      body { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; line-height: 1.4; padding: 24px; }
      pre  { background: #0F7450; color: #e6edf3; padding: 16px; border-radius: 12px; overflow: auto; }
      .hint { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; margin-bottom: 12px; color: #444; }
    </style>
  </head>
  <body>
    
    <pre>GameBot-AI/
│
├── .github/
│   ├── workflows/
│   │   └── python-ci.yml      # CI/CD Automated Testing pipeline
│   └── dependabot.yml         # Auto-updates AI dependencies safely
├── agents/                    # RL Models (PPO, DQN, SAC architectures)
├── datasets/                  # Human gameplay replays (.h5) for Imitation Learning
├── environment/               # Gymnasium custom envs wrapping the game
├── inputs/                    # Input simulation (vgamepad, pydirectinput)
├── memory/                    # Pymem scripts & Cheat Engine offset pointers (.json)
├── models/
│   ├── best_model/            # Auto-saved highest scoring models
│   ├── checkpoints/           # Routine failsafe backups during training
│   └── saved_models/          # Final trained model weights
├── tests/                     # Pytest scripts to verify logic
├── utils/                     # Reward functions, loggers, helper scripts
├── vision/                    # Screen capture (mss/dxcam) & OpenCV scripts
│
├── .gitattributes             # Git LFS rules for large AI models & datasets
├── .gitignore                 # Blocks heavy weights, screenshots, and system logs
├── pyproject.toml             # Ruff linter rules and modern project config
├── requirements.txt           # Python dependencies
├── record_human.py            # Script to record your own gameplay to a dataset
├── train.py                   # Master script (Parallel Envs, Frame Stacking, Callbacks)
└── play.py                    # Script to let the trained AI play the game live</pre>
  </body>
</html>
