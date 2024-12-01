import time
import pyttsx3


def speak_time():
    # Initialize text-to-speech engine
    engine = pyttsx3.init()

    # Optional: Configure the speech engine
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[106].id)  # Use the first available voice
    engine.setProperty('rate', 150)  # Adjust speed (default is around 200)

    try:
        while True:
            # Get the current time
            current_time = time.strftime("%I:%M %p")  # Format: HH:MM AM/PM
            message = f"The time is now {current_time}"

            # Print the message for reference
            print(message)

            # Speak the message
            engine.say(message)
            engine.runAndWait()

            # Wait for 5 minutes
            time.sleep(10)  # 300 seconds = 5 minutes

    except KeyboardInterrupt:
        print("\nProgram stopped by user.")


if __name__ == "__main__":
    speak_time()