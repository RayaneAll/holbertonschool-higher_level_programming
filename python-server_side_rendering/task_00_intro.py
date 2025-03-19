import os

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and a list of attendees.
    
    Args:
        template (str): The invitation template containing placeholders.
        attendees (list): A list of dictionaries with attendee details.
    
    Returns:
        None
    """

    # Check if the template is a string
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return

    # Check if attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    # Check if the template is empty
    if not template.strip():
        print("Error: Template is empty, no output files generated.")
        return

    # Check if the attendees list is empty
    if not attendees:
        print("Error: No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Replace placeholders with actual values or "N/A" if missing
        filled_template = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A")
        )

        # Define output file name
        output_filename = f"output_{index}.txt"

        # Write to the file
        try:
            with open(output_filename, "w") as output_file:
                output_file.write(filled_template)
            print(f"Generated: {output_filename}")
        except Exception as e:
            print(f"Error writing to {output_filename}: {e}")

# Example usage
if __name__ == "__main__":
    # Read the template from a file
    template_path = "template.txt"

    if not os.path.exists(template_path):
        print(f"Error: Template file '{template_path}' not found.")
    else:
        with open(template_path, "r") as file:
            template_content = file.read()

        # Example list of attendees
        attendees = [
            {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
            {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
            {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
        ]

        # Call the function
        generate_invitations(template_content, attendees)
