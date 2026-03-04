import os
import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import SubprocVecEnv, VecFrameStack
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.callbacks import CheckpointCallback, EvalCallback

# Import your custom gym environment wrapped around the game
from environment.game_env import GameEnvironment

if __name__ == "__main__":
    print("Initializing Advanced GameBot-AI Pipeline...")

    # 1. PARALLEL VECTORIZATION (Run 4 games at once)
    num_envs = 4
    env = make_vec_env(GameEnvironment, n_envs=num_envs, vec_env_cls=SubprocVecEnv)

    # 2. FRAME STACKING (AI perceives motion/velocity across 4 frames)
    env = VecFrameStack(env, n_stack=4)

    # 3. DIRECTORY SETUP
    os.makedirs("./models/checkpoints/", exist_ok=True)
    os.makedirs("./models/best_model/", exist_ok=True)

    # 4. FAILSAFE CHECKPOINTS (Save every 100k steps)
    checkpoint_callback = CheckpointCallback(
        save_freq=max(100_000 // num_envs, 1), 
        save_path='./models/checkpoints/',
        name_prefix='gamebot_ppo'
    )

    # 5. BEST MODEL EVALUATION (Test AI periodically and save the best run)
    eval_callback = EvalCallback(
        env,
        best_model_save_path='./models/best_model/',
        log_path='./logs/eval_results/',
        eval_freq=max(25_000 // num_envs, 1),
        deterministic=True,
        render=False
    )

    # 6. THE THINKING AGENT (CNN feature extractor + PPO RL logic)
    # *Note: If using Dataset Tools (Imitation Learning), load your cloned weights here first*
    model = PPO(
        "CnnPolicy", 
        env, 
        verbose=1, 
        tensorboard_log="./tb_logs/",
        learning_rate=0.0003,
        n_steps=2048,
        batch_size=64
    )

    print("Beginning Deep Reinforcement Learning Loop...")
    
    # 7. EXECUTE TRAINING
    model.learn(
        total_timesteps=5_000_000, 
        callback=[checkpoint_callback, eval_callback]
    )

    # 8. SAVE FINAL WEIGHTS
    model.save("models/saved_models/gamebot_final")
    print("Training Complete. Model Saved!")
