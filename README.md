# 🤖 Smart Desktop Assistant

An interactive terminal-based assistant that combines voice interaction, data analysis, and web information retrieval.

## 🚀 Key Features
* **Voice Feedback**: Uses `pyttsx3` for real-time speech responses to handle user interactions.
* **Matrix Operations**: Leverages `NumPy` for creating and analyzing matrices (Min/Max values).
* **Information Retrieval**: Integrated with `Wikipedia API` to fetch summaries on any topic.
* **Automated Reporting**: Generates and appends results to a local text report (`matrix_output.txt`).

## 🛠️ Built With
- **Python**: Core logic.
- **NumPy**: Data processing and matrix manipulation.
- **pyttsx3**: Text-to-Speech (TTS) engine.
- **Wikipedia-API**: Online data fetching.

## 📂 Project Structure
- `smart_assistant.py`: Main script containing all logic and voice commands.
- `matrix_output.txt`: Generated report file storing analysis and search history.
- `requirements.txt`: List of necessary libraries for the project.

## 📋 How to Run
1. Install dependencies: `pip install numpy pyttsx3 wikipedia`
2. Run the script: `python smart_assistant.py`
