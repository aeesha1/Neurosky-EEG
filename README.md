# EEG Data Collection App

The **EEG Data Collection App** is designed for students and researchers to capture, process, and analyze EEG signals using the Mindwave headset. This app simplifies EEG data collection and provides tools to save and visualize the results.

---

## Features

- Connects seamlessly with the Mindwave headset via a COM port.
- Configurable settings include sampling frequency, filter cut-offs, task duration, and more.
- Supports multiple motor imagery and EEG tasks.
- Saves both raw and filtered EEG data into organized CSV files.
- Generates and saves visual plots of EEG signals for each participant.

---

## Prerequisites

1. **Hardware**:
   - Mindwave headset.
   - Bluetooth dongle (or equivalent for connection).

2. **Software**:
   - Windows.
   - Python.

3. **Dependencies**:
   - The app utilizes the `mindwave` library from Moonshot Lab Berkely  to interface with the Mindwave headset. 

   **Credit:** The package is open-source and can be found at: [Mindwave Python Parser](https://github.com/BarkleyUS/mindwave-python). All rights to the package remain with the original author.

---

## Installation

### Running from Source
1. Clone this repository:
   ```bash
   git clone https://github.com/aeesha1/Neurosky-EEG
   cd eeg-data-collection
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python app.py
   ```

---

## How to Use

1. Ensure the Mindwave headset is turned on and connected via Bluetooth.
2. Launch the Python script.
3. Provide the requested parameters such as COM port, sampling frequency, and tasks.
4. During the experiment, follow the prompts to complete tasks.
5. After the experiment, enter a participant ID to save results.

Results, including a CSV file and EEG plots, will be saved in the `eeg_experiment_data/<participant_id>` folder.

---

## Acknowledgments

- **Mindwave Package**: Special thanks to Moonshot Lab, Barkley for developing the [mindwave](https://github.com/BarkleyUS/mindwave-python) package, which makes interfacing with the Mindwave headset simple and efficient.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for improvements.

---

## Contact

For questions or feedback, please contact [your email or GitHub profile link].
