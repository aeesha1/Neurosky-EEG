import logging
import winsound

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


# Buzzer
def play_buzzer():
    winsound.Beep(440, 1000)  # Frequency: 440 Hz, Duration: 1000 ms

# Print experiment instructions
def print_instructions(task_duration, rest_duration, num_trials):
    logging.info(f"""
    Welcome to the Motor Imagery Experiment.
    
    Please sit comfortably, focus on imagining the body part as vividly as possible during the task periods.

    Tasks:
    - Imagine moving the specified body part during task periods.
    - Relax during rest periods.

    Each task lasts {task_duration} seconds, followed by {rest_duration} seconds of rest.
    There are {num_trials} trials in total.

    The experiment will start shortly. Please follow the on-screen prompts.
    """)