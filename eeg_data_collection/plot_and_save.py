import os
import csv
import logging
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def save_data(participant_id, raw_data, filtered_data, task_labels, timestamps):
    """
    Save EEG data to a CSV file and the plot to an image file in a directory structure organized by participant ID.
    
    Parameters:
        participant_id (str): Unique identifier for the participant.
        raw_data (list): List of raw EEG data points.
        filtered_data (list): List of filtered EEG data points.
        task_labels (list): List of task labels corresponding to the EEG data.
        timestamps (list): List of timestamps for the EEG data.
    """
    # Create main directory
    main_directory = 'eeg_experiment_data'
    os.makedirs(main_directory, exist_ok=True)

    # Create subdirectory for participant
    participant_directory = os.path.join(main_directory, participant_id)
    os.makedirs(participant_directory, exist_ok=True)

    # Save CSV file
    csv_filename = os.path.join(participant_directory, f'eeg_data_{participant_id}.csv')
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'Raw EEG', 'Filtered EEG', 'Task'])
        for t, raw, filtered, label in zip(timestamps, raw_data, filtered_data, task_labels):
            writer.writerow([t, raw, filtered, label])
    logging.info(f"Data saved to {csv_filename}")

    # Save and plot the EEG data
    plot_filename = os.path.join(participant_directory, f'eeg_plot_{participant_id}.png')
    plt.figure(figsize=(12, 8))

    # Define colors for tasks
    color_palette = cm.get_cmap('tab10')  # Use a colormap with 10 distinct colors
    unique_tasks = list(set(task_labels))
    task_colors = {task: color_palette(i / len(unique_tasks)) for i, task in enumerate(unique_tasks)}
    
    task_start_times = {}

    # define x-axis markers
    x_markers = [np.arange((min(timestamps), max(timestamps)+1, 2.0))]

    # Plot original EEG
    plt.subplot(2, 1, 1)
    plt.plot(timestamps, raw_data, label='Original EEG')
    for i in range(1, len(timestamps)):
        if task_labels[i] != task_labels[i - 1]:
            task_start = task_labels[i]
            if task_start not in task_start_times:
                task_start_times[task_start] = timestamps[i]
        
        # Plot task start marker
        plt.axvline(x=timestamps[i], color=task_colors[task_start], linestyle='--', label=f'{task_start} start')

    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude (µV)')
    plt.title('Original EEG Signal')
    plt.xticks(x_markers)
    plt.legend()

    # Plot filtered EEG
    task_start_times.clear()
    plt.subplot(2, 1, 2)
    plt.plot(timestamps, filtered_data, label='Filtered EEG')
    for i in range(1, len(timestamps)):
        if task_labels[i] != task_labels[i - 1]:
            task_start = task_labels[i]
            if task_start not in task_start_times:
                task_start_times[task_start] = timestamps[i]   # Track start time
 
        # plot task start marker
        plt.axvline(x=timestamps[i], color=task_colors[task_start], linestyle='--', label=f'{task_start} start')
        
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude (µV)')
    plt.title('Filtered EEG Signal')
    plt.xticks(x_markers)
    plt.legend()

    plt.tight_layout()

    # Save plot
    plt.savefig(plot_filename, dpi=300)
    plt.close()  # Close the plot to free memory
    logging.info(f"Plot saved to {plot_filename}")
