# JUENO
JUENO-AI: The Ultimate Video Game AI Blueprint
<pre style="background:#0d1117; color:#c9d1d9; padding:16px; border-radius:8px; overflow:auto;">
JUENO-AI/
│
├── .github/
│   ├── workflows/
│   │   └── python-ci.yml      # CI/CD Automated Testing
│   └── dependabot.yml         # Auto-updates AI dependencies
├── agents/                    # SB3 Models (PPO, DQN, SAC architectures)
├── environment/               # Gymnasium custom envs wrapping the game
├── vision/                    # Screen capture (mss/dxcam) & OpenCV scripts
├── memory/                    # Pymem scripts & Cheat Engine offset JSONs
├── inputs/                    # vgamepad / pydirectinput simulation scripts
├── utils/                     # Reward function logic, loggers, helpers
├── tests/                     # Pytest scripts to verify logic
│
├── .gitattributes             # Git LFS rules for large AI models
├── .gitignore                 # Blocks heavy model weights and logs
├── pyproject.toml             # Ruff linter and modern project config
├── requirements.txt           # Python dependencies
├── train.py                   # Main script to start RL training
└── play.py                    # Script to let the trained AI play the game
</pre>
