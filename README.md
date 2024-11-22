# Meeting Minutes and Task Generator

This project automates the generation of meeting minutes and task lists from transcribed audio using OpenAI's GPT-4 API.

## Features
- Automatically generates meeting minutes and tasks.
- Outputs results to a single text file.
- Modular and easy-to-extend codebase.

## Setup
1. Clone this repository:
git clone https://github.com/your-username/meeting-minutes.git cd meeting-minutes

2. Install dependencies:
pip install -r requirements.txt

3. Add your OpenAI API key in the `main.py` file.

4. Run the script:
python src/main.py

## File Structure
- `src/main.py`: Main script to generate meeting minutes and tasks.
- `src/utils.py`: Utility functions for file handling.
- `transcription_samples/`: Sample transcription files for testing.

## License
MIT License