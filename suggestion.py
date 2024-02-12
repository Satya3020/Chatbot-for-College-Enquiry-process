import tkinter as tk
from tkinter import ttk

# Create a dictionary of courses with their associated interests, hobbies, and achievements
courses = {
    'Computer Science Engineering': {
        'interests': ['programming', 'gaming', 'mathematics', 'web development', 'Artificial intelligence', 'Machine Learning', 'software development'],
        'hobbies': ['coding projects', 'robotics'],
        'achievements': ['programming competitions', 'hackathons']
    },
     'Mechanical Engineering': {
        'interests': ['cars', 'machines'],
        'hobbies': ['building machines', 'mechanical puzzles'],
        'achievements': ['robotics competitions', 'engineering projects']
    },
    'Electrical and Electronics Engineering': {
        'interests': ['circuits', 'robotics', 'Internet of Things', 'VLSI Design', 'Renewable energy resources'],
        'hobbies': [],
        'achievements': []
    },
    'Information technology': {
        'interests': ['programming', 'Data analysis', 'cybersecurity', 'cloud computing', 'computer networks', 'Blockchain'],
        'hobbies': [],
        'achievements': []
    },
    'Electronics and communication Engineering': {
        'interests': ['circuits', 'embedded systems', 'photonics', 'VLSI Design', 'wireless communications'],
        'hobbies': [],
        'achievements': []
    }

}


# Define a function to suggest courses based on interests, hobbies, and achievements
def suggest_course(interests, hobbies, achievements):
    suggested_courses = []
    for course, course_data in courses.items():
        if any(interest in course_data['interests'] for interest in interests):
            suggested_courses.append(course)
        elif any(hobby in course_data['hobbies'] for hobby in hobbies):
            suggested_courses.append(course)
        elif any(achievement in course_data['achievements'] for achievement in achievements):
            suggested_courses.append(course)
    suggested_courses = list(set(suggested_courses))
    if suggested_courses:
        return f"You could consider these courses: {', '.join(suggested_courses)}"
    else:
        return "Sorry, there are no courses available for your interests, hobbies, and achievements."


# Define a function to interact with the user
def chat():
    def on_submit():
        interests = [interests_combo.get()]
        hobbies = [hobbies_combo.get()]
        achievements = [achievements_combo.get()]
        result = suggest_course(interests, hobbies, achievements)
        result_label.config(text=result)

    # Create GUI
    window = tk.Tk()
    window.title("Course Suggestion Chatbot")
    window.geometry("500x400")
    
    
    title_label = ttk.Label(window, text="LICET - Course Suggestion Bot  ", font=("TkDefaultFont", 16), justify="center")
    title_label.grid(column=0, row=0, columnspan=2, padx=130, pady=20)

    # Create input fields
    interests_label = ttk.Label(window, text="Select your interests:")
    interests_label.grid(column=0, row=1, padx=40, pady=10, sticky=tk.W)

    interests_values = ["programming", 'cars', 'machines', 'circuits', 'robotics', 'Internet of Things', 'VLSI Design', 'circuits', 'embedded systems', 'photonics', 'VLSI Design', 'wireless communications', 'Renewable energy resources', "gaming", "mathematics", 'Data analysis', 'cybersecurity', 'cloud computing', 'computer networks', 'Blockchain', "web development", "Artificial intelligence", "Machine Learning", "software development"]
    interests_combo = ttk.Combobox(window, values=interests_values, state='readonly')
    interests_combo.current(0)
    interests_combo.grid(column=1, row=1, padx=0, pady=10, sticky=tk.W)

    hobbies_label = ttk.Label(window, text="Select your hobbies:")
    hobbies_label.grid(column=0, row=2, padx=40, pady=10, sticky=tk.W)

    hobbies_values = ["reading", "writing", "photography", "painting", "traveling", "cooking", "music", "dance", "sports", "gardening", "fishing", "camping", "hiking"]
    hobbies_combo = ttk.Combobox(window, values=hobbies_values, state='readonly')
    hobbies_combo.current(0)
    hobbies_combo.grid(column=1, row=2, padx=0, pady=10, sticky=tk.W)

    achievements_label = ttk.Label(window, text="Select your achievements:")
    achievements_label.grid(column=0, row=3, padx=40, pady=10, sticky=tk.W)

    achievements_values = ["programming competitions", "hackathons"]
    achievements_combo = ttk.Combobox(window, values=achievements_values, state='readonly')
    achievements_combo.current(0)
    achievements_combo.grid(column=1, row=3, padx=0, pady=10, sticky=tk.W)

    # Create submit button
    submit_button = ttk.Button(window, text="Get Course Suggestions", command=on_submit, style='Submit.TButton')
    submit_button.grid(column=0, row=4, columnspan=2, padx=0, pady=10)

    # Create result label
    result_label = ttk.Label(window, text="", font=("Arial", 11), wraplength=350, justify="center")
    result_label.grid(column=0, row=5, columnspan=2, padx=10, pady=20)

    window.mainloop()

# Start the chatbot
chat()