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
external_tools_by_account = canvasild.fetch_external_tools_by_account(account_id)

for external_tool in external_tools_by_course:
    print(f'External tool for course {course_id} is {external_tool["id"]}')

assignments = canvasild.fetch_assignments(course_id)
for assignment in assignments:
    print(f'Assignment id for course {course_id} is {assignment["id"]}')
    print(f'External Tool id (content_id) id for Assignment {assignment["id"]} is {assignment["external_tool_tag_attributes"]["content_id"]}')

new_url = "https://flatiron-enterprise.illumidesk.com"
new_content_id = 1305

new_assignment = {}
new_assignment['external_tool_tag_attributes'] = {}
new_assignment['external_tool_tag_attributes']['url'] = new_url
new_assignment['external_tool_tag_attributes']['content_id'] = new_content_id

#payload={'assignment[external_tool_tag_attributes]': 'content_id: 1305',}
external_tool = {
    'url': 'https://flatiron-enterprise.illumidesk.com', 
    'new_tab': True, 
    'resource_link_id': '3722e75fb935a1f94f07e4ca027e5459263543d4', 
    'external_data': '', 
    'content_type': 'ContextExternalTool', 
    'content_id': 1305, 
    'custom': None,
}

new_assignment_test = {
    'assignment[name]': 'Foo Bar',
    'assignment[external_tool_tag_attributes][url]': external_tool["url"],
    'assignment[external_tool_tag_attributes][content_id]': external_tool["content_id"],
    'assignment[external_tool_tag_attributes][content_type]': external_tool["content_type"],
    'assignment[peer_reviews]': True,
}

response_update_assignment = canvasild.update_assignment(course_id, 980, new_assignment_test)

print(f'New assignment response {response_update_assignment}')
