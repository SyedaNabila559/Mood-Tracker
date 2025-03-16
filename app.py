import json
import datetime
import streamlit as st

class MoodTracker:
    def __init__(self):
        self.moods = []
        self.filename = "mood_tracker.json"
        self.load_moods()

    def load_moods(self):
        """Load mood data from a file."""
        try:
            with open(self.filename, "r") as file:
                self.moods = json.load(file)
        except FileNotFoundError:
            self.moods = []
        except json.JSONDecodeError:
            self.moods = []

    def save_moods(self):
        """Save mood data to a file."""
        with open(self.filename, "w") as file:
            json.dump(self.moods, file, indent=4)

    def add_mood(self, mood_choice):
        """Add a new mood entry."""
        mood_dict = {
            "1": {"mood": "Happy", "quote": "Happiness is not something ready-made. It comes from your own actions. - Dalai Lama"},
            "2": {"mood": "Sad", "quote": "Sadness is but a wall between two gardens. - Kahlil Gibran"},
            "3": {"mood": "Excited", "quote": "The best way to predict the future is to create it. - Abraham Lincoln"},
            "4": {"mood": "Love", "quote": "Love is not about possession. Love is about appreciation. - Osho"},
            "5": {"mood": "Tired", "quote": "Rest is not idleness, and to lie on the grass under the trees on a summer's day, listening to the murmur of the water, is by no means a waste of time. - John Lubbock"},
            "6": {"mood": "Frustrated", "quote": "Frustration is a sign that you're getting closer to something big. - Unknown"},
            "7": {"mood": "Thoughtful", "quote": "The unexamined life is not worth living. - Socrates"},
            "8": {"mood": "Cool", "quote": "Being cool is being yourself. - Unknown"}
        }

        mood_data = mood_dict.get(mood_choice)
        if mood_data:
            mood = mood_data["mood"]
            quote = mood_data["quote"]
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.moods.append({"mood": mood, "quote": quote, "timestamp": timestamp})
            self.save_moods()
            return mood, quote
        else:
            return None, None

    def display_moods(self):
        """Display all mood entries."""
        if not self.moods:
            return "No mood data found."

        mood_history = ""
        for mood_entry in self.moods:
            mood_history += f"Date: {mood_entry['timestamp']}\n"
            mood_history += f"Mood: {mood_entry['mood']}\n"
            mood_history += f"Quote: {mood_entry['quote']}\n\n"

        return mood_history


def main():
    st.title("🌈 Mood Tracker 🌈")

    # Initialize the mood tracker
    tracker = MoodTracker()

    # Display the menu
    menu_choice = st.selectbox("What would you like to do?", ["Add a new mood", "View mood history", "Exit"])

    if menu_choice == "Add a new mood":
        st.subheader("Select your mood for today:")
        mood_choice = st.selectbox("Choose a mood", ["", "😊 Happy", "😢 Sad", "😆 Excited", "❤️ Love", "😴 Tired", "😤 Frustrated", "🤔 Thoughtful", "😎 Cool"])

        if st.button("Save Mood"):
            mood_number = {
                "😊 Happy": "1",
                "😢 Sad": "2",
                "😆 Excited": "3",
                "❤️ Love": "4",
                "😴 Tired": "5",
                "😤 Frustrated": "6",
                "🤔 Thoughtful": "7",
                "😎 Cool": "8"
            }.get(mood_choice)

            if mood_number:
                mood, quote = tracker.add_mood(mood_number)
                if mood:
                    st.success(f"Mood saved! Your mood today is: {mood} 😊")
                    st.write(f"Quote for today: {quote}")
            else:
                st.warning("Please select a valid mood.")
    
    elif menu_choice == "View mood history":
        st.subheader("Your Mood History:")
        history = tracker.display_moods()
        st.text_area("Mood History", value=history, height=300)

    elif menu_choice == "Exit":
        st.write("Goodbye! 😊")

if __name__ == "__main__":
    main()
