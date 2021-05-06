# Import the Canvas class
import os

from lmsclient import CanvasClient

# Initialize CanvasLmsClient client
API_KEY =  ""
API_URL = "https://illumidesk.instructure.com"

# Initialize a new Canvas object
canvasild = CanvasClient(API_KEY, instructure_domain='illumidesk.instructure.com')

course_id = 329
account_id = 1

# Get a list of all course
external_tools_by_course = canvasild.fetch_external_tools_by_course(course_id)

# Get a list of all accounts
external_tools_by_account = canvasild.fetch_external_tools_by_account(account_id)

# Get external tools info
for external_tool in external_tools_by_course:
    print(f'External tool for course {course_id} is {external_tool["id"]}')

# Get the list of assignments for a course by course id
assignments = canvasild.fetch_assignments(course_id)
for assignment in assignments:
    print(f'Assignment id for course {course_id} is {assignment["id"]}')
    print(f'External Tool id (content_id) id for Assignment {assignment["id"]} is {assignment["external_tool_tag_attributes"]["content_id"]}')

# Create a dictionary that represents the external tool
external_tool = {
    'url': 'https://flatiron-enterprise.illumidesk.com', 
    'new_tab': True, 
    'resource_link_id': '3722e75fb935a1f94f07e4ca027e5459263543d4', 
    'external_data': '', 
    'content_type': 'ContextExternalTool', 
    'content_id': 1305, 
    'custom': None,
}

# Update the assignment
new_assignment_test = {
    'assignment[name]': 'Foo Bar',
    'assignment[external_tool_tag_attributes][url]': external_tool["url"],
    'assignment[external_tool_tag_attributes][content_id]': external_tool["content_id"],
    'assignment[external_tool_tag_attributes][content_type]': external_tool["content_type"],
    'assignment[peer_reviews]': True,
}

# Get the new assignment and print it's contents
response_update_assignment = canvasild.update_assignment(course_id, 980, new_assignment_test)

print(f'New assignment response {response_update_assignment}')
