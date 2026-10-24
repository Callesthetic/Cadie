# Cadie — Personal Voice Assistant 🎙️

Cadie is a Python-based personal voice assistant that listens to voice commands and responds using speech. It can tell the time, search Wikipedia, open websites, play songs on YouTube, tell jokes, perform basic arithmetic, fetch weather information, and set timers.

This project is a hands-on exploration of Python, speech recognition, text-to-speech, API integration, regular expressions, and multithreading.

## ✨ Features

- **Voice interaction:** Listens to spoken commands through a microphone and converts speech into text.
- **Text-to-speech:** Responds aloud using `pyttsx3` and also prints responses in the terminal.
- **Personalized greetings:** Asks for your name and greets you according to the time of day.
- **Time:** Tells you the current time.
- **Wikipedia search:** Retrieves and reads a summary of a requested topic.
- **Website shortcuts:** Opens YouTube, Google, and Spotify in your default browser.
- **YouTube playback:** Searches for a requested song or video and plays the first video on YouTube.
- **Jokes:** Tells random jokes using `pyjokes`.
- **Basic calculations:** Handles arithmetic operations such as addition, subtraction, multiplication, and division using spoken expressions.
- **Weather updates:** Retrieves the requested city's current weather description, temperature, feels-like temperature, and humidity using the OpenWeather API.
- **Timers:** Sets timers in seconds, minutes, or hours and announces when the time is up. Timers run in separate background threads.

## 🛠️ Tech Stack

- **Language:** Python
- **Speech recognition:** SpeechRecognition
- **Text-to-speech:** pyttsx3
- **Information retrieval:** Wikipedia
- **Web automation:** PyWhatKit and Python's `webbrowser`
- **Jokes:** PyJokes
- **Weather data:** OpenWeather API
- **HTTP requests:** Requests
- **Environment variables:** python-dotenv
- **Other modules:** datetime, time, threading, re, and os

## 📋 Prerequisites

Before running Cadie, make sure you have:

- Python installed on your computer.
- Working microphone and audio output device.
- Stable internet connection for speech recognition and online features.
- An OpenWeather API key for weather updates.

## 🚀 Getting Started

### 1. Clone the repository

Open a terminal and run:

```bash
git clone https://github.com/Callesthetic/Cadie.git
```

Navigate to the project directory:

```bash
cd Cadie
```

### 2. Install the dependencies

Install the required Python packages:

```bash
python -m pip install SpeechRecognition pyttsx3 wikipedia pyjokes pywhatkit requests python-dotenv PyAudio
```

`PyAudio` is used by the microphone input functionality. Its installation may depend on your Python version and Windows environment.

### 3. Configure the weather API

Cadie uses the OpenWeather API to retrieve current weather information.

1. Create an account at [OpenWeather](https://openweathermap.org/api).
2. Obtain an API key.
3. Create a file named `.env` in the project root directory, alongside `First.py.py`.
4. Add the following line to the `.env` file:

```env
Openweather_api_key=your_api_key_here
```

Replace `your_api_key_here` with your actual API key.

**Important:** Keep your API key private. Do not commit your `.env` file to GitHub. The repository's `.gitignore` is configured to exclude it.

### 4. Run Cadie

Run the Python script from the project directory:

```bash
python First.py.py
```

Cadie will ask for your name, greet you based on the current time, and begin listening for voice commands.

## 🗣️ Example Voice Commands

| What you want to do | Example command |
|---|---|
| Ask for the time | "What is the time?" |
| Search Wikipedia | "Wikipedia Python programming" |
| Open YouTube | "Open YouTube" |
| Open Google | "Open Google" |
| Open Spotify | "Open Spotify" |
| Play a song on YouTube | "Play [song name]" |
| Hear a joke | "Tell me a joke" |
| Calculate a sum | "Calculate 25 plus 15" |
| Multiply numbers | "What is 8 times 7?" |
| Divide numbers | "Calculate 20 divided by 4" |
| Get weather information | "What's the weather?" wait for the follow-up question and proceed with the city name |
| Set a timer | "Set a timer for 2 minutes" |
| Exit the assistant | "Bye" or "Exit" |

Commands are processed using speech recognition, so results may vary depending on microphone quality, pronunciation, and background noise.

## 📁 Project Structure

```text
Cadie/
├── First.py.py    # Main voice assistant script
├── .gitignore     # Excludes private and unnecessary files
├── LICENSE        # GNU General Public License v2.0
├── README.md      # Project documentation
└── .env           # Private API key configuration (created locally)
```

The `.env` file is created by the user and should not be uploaded to the repository.

## 🔐 Privacy and Security

- The OpenWeather API key is loaded from a local environment file rather than being written directly into the Python script.
- Speech recognition uses Google's online recognition service through the SpeechRecognition library.
- Wikipedia searches and weather requests require internet access.
- Arithmetic expressions are evaluated using Python's `eval()`.

## 🚧 Current Limitations

- Cadie relies on a microphone and may not recognize every spoken command correctly.
- Online features require an active and stable internet connection.
- Weather updates require a valid OpenWeather API key.
- Spotify is opened in the browser; direct Spotify playback control is not implemented.
- Timers are temporary and run only while the program is running.
- The assistant currently supports a defined set of commands rather than unrestricted conversational requests.

## 🔮 Future Improvements

Potential improvements for future versions include:

- Expand the range of supported voice commands.
- Improve speech recognition and error handling.
- Add persistent reminders and task management.
- Make the code more modular and maintainable.
- Integrate additional useful services and features.

These are planned improvements, not features currently implemented.

## 👩‍💻 Author

**Divyanshi Verma**

GitHub: [@Callesthetic](https://github.com/Callesthetic)

## 📄 License

This project is licensed under the **GNU General Public License v2.0 (GPL-2.0)**. See the [LICENSE](LICENSE) file for details.
