from pyscript import document, when 

CLUB_DATA = {
    "Art Club": {
        "Description": "A club for visual artists who enjoy painting, drawing, and sculpting.",
        "Meeting Time": "Every Tuesday 4:00-5:30 PM",
        "Location": "Art Studio (Room 201)",
        "Club Moderator": "Ms. Cruz",
        "Number of Members": 35,
        "Category": "Arts"
    },
    "Glee Club": {
        "Description": "An opportunity for students to practice vocal performance and harmony.",
        "Meeting Time": "Every Thursday 3:30-5:00 PM",
        "Location": "Music Room (Room 105)",
        "Club Moderator": "Mr. Reyes",
        "Number of Members": 28,
        "Category": "Performing Arts"
    },
    "Dance Club": {
        "Description": "Focuses on various dance styles, choreography, and performance.",
        "Meeting Time": "Every Monday and Friday 4:00-6:00 PM",
        "Location": "Gymnasium Annex",
        "Club Moderator": "Ms. Garcia",
        "Number of Members": 42,
        "Category": "Performing Arts"
    },
    "ComArts": {
        "Description": "A communication arts club dedicated to public speaking, debate, debate, and scriptwriting.",
        "Meeting Time": "Every Wednesday 3:30-4:45 PM",
        "Location": "Speech Lab (Room 307)",
        "Club Moderator": "Mr. Tan",
        "Number of Members": 22,
        "Category": "Academic"
    },
    "COCC": {
        "Description": "The Cadet Officers Candidate Corps, focused on leadership and discipline.",
        "Meeting Time": "Every Saturday 8:00 AM-12:00 PM",
        "Location": "School Grounds and Field",
        "Club Moderator": "Sgt. Dela Rosa",
        "Number of Members": 50,
        "Category": "Service"
    },
}

@when("click", selector="#show-info-button")
def show_club_info(event=None): 
    club_select_element = document.getElementById("club-select")
    selected_club_name = club_select_element.value
    club_details = CLUB_DATA.get(selected_club_name, None)
    
    output_element = document.getElementById("club-info")
    
    if club_details:
        info_text = f"--- {selected_club_name} ---\n"
        info_text += f"Description: {club_details['Description']}\n"
        info_text += f"Meeting Time: {club_details['Meeting Time']}\n"
        info_text += f"Location: {club_details['Location']}\n"
        info_text += f"Club Moderator: {club_details['Club Moderator']}\n"
        info_text += f"Number of Members: {club_details['Number of Members']}\n"
        info_text += f"Category: {club_details['Category']}"
        
        output_element.textContent = info_text 
    else:
        output_element.textContent = "Error: Club details not found."

def setup_initial_club():
    club_select_element = document.getElementById("club-select")
    selected_club_name = club_select_element.value
    club_details = CLUB_DATA.get(selected_club_name, None)

    output_element = document.getElementById("club-info")

    if club_details:
        info_text = f"--- {selected_club_name} ---\n"
        info_text += f"Description: {club_details['Description']}\n"
        info_text += f"Meeting Time: {club_details['Meeting Time']}\n"
        info_text += f"Location: {club_details['Location']}\n"
        info_text += f"Club Moderator: {club_details['Club Moderator']}\n"
        info_text += f"Number of Members: {club_details['Number of Members']}\n"
        info_text += f"Category: {club_details['Category']}"
        output_element.textContent = info_text 
    else:
        output_element.textContent = "Select a club and click the button to see the details."

setup_initial_club()