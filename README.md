# JUENO
GameBot-AI: The Ultimate Video Game AI Blueprint
GameBot-AI/
│
├── agents/                 # The "Thinking" Agent models (PPO, DQN, SAC)
├── environment/            # Gymnasium custom envs wrapping the game
├── vision/                 # Computer Vision & Screen capture scripts
├── memory/                 # Pymem scripts & offset pointers 
├── inputs/                 # Input simulation (Virtual gamepad, keyboard)
├── utils/                  # Reward function logic, loggers, helpers
├── models/                 # Saved PyTorch/SB3 model weights (.zip / .pt)
├── train.py                # Main script to start RL training
├── play.py                 # Script to let the trained AI play the game
├── requirements.txt        # Python dependencies
├── .gitignore              # Ignore models/, __pycache__/, etc.
└── README.md               # Project documentation
