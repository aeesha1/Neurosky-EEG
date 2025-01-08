import time
import mindwave
import numpy as np
from plot_and_save import save_data
from filters import * 
from utils import *


# Collect EEG data
def collect_data(headset, duration, label, buffer, timestamps, task_labels, fs):
    start_time = time.time()
    while time.time() - start_time < duration:
        raw_eeg = headset.raw_value
        buffer.append(raw_eeg)
        timestamps.append(time.time() - start_time)
        task_labels.append(label)
        time.sleep(1 / fs)


# Main experiment logic
def run_experiment():
    try:
        # Interactive setup
        com_port = input("Enter COM port for the Mindwave headset (default: COM6): ").strip().upper() or "COM6"
        fs = int(input("Enter sampling frequency (Hz, default: 512Hz): ") or 512)
        lowcut = float(input("Enter low cut-off frequency for bandpass filter (Hz, default: 8.0Hz): ") or 8.0)
        highcut = float(input("Enter high cut-off frequency for bandpass filter (Hz, default: 30.0Hz): ") or 30.0)
        num_trials = int(input("Enter the number of trials (default: 2): ") or 2)
        task_duration = int(input("Enter task duration (seconds, default: 5s): ") or 5)
        rest_duration = int(input("Enter rest duration (seconds, default: 5s): ") or 5)
        tasks = ""
        while not tasks.strip():
            tasks = input("Enter the task or tasks(comma seperated if more than 1) e.g: left_leg")
        if not tasks:
            logging.info("This field is required")
            
        tasks_li = tasks.strip().split(",")
            

        # Initialize headset
        logging.info(f"Connecting to Mindwave headset on {com_port}...")
        headset = mindwave.Headset(com_port)
        time.sleep(2)

        # Prepare variables
        raw_data = []
        timestamps = []
        task_labels = []
        
        

        print_instructions(task_duration, rest_duration, num_trials)

        # Conduct trials
        for trial in range(1, num_trials + 1):
            logging.info(f"Starting Trial {trial}...")
           
            for task in tasks_li:
                task_type = task.replace('_', ' ').title()
                logging.info(f"\n{task_type} Motor Imagery \n\r Duration: {task_duration}sec \n\r Cue: Imagine moving your left leg.")
                play_buzzer()
                collect_data(headset, task_duration, task, raw_data, timestamps, task_labels, fs)
                
                # Rest period after each task
                if task != tasks_li[-1]:
                    task_type = tasks_li[-1].replace('_', ' ').title()
                    print(f"\nRelax and prepare for the next task, {task_type} motor imagery. \n\r Duration: {task_duration}sec")
                    collect_data(headset, rest_duration, 'rest', raw_data, timestamps, task_labels, fs)

        # Process data
        raw_data_np = np.array(raw_data)
        filtered_data = bandpass_filter(raw_data_np, lowcut, highcut, fs)
        filtered_data = notch_filter(filtered_data, fs)

        # Save data
        participant_id = input("Enter Participant ID (e.g., P01): ").lower()
        save_data(participant_id, raw_data, filtered_data, task_labels, timestamps)

    except Exception as e:
        logging.error(f"An error occurred: {e}")

    finally:
        headset.stop()
        logging.info("Experiment completed.")

# Entry point
if __name__ == "__main__":
    run_experiment()
