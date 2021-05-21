# LMS Client API

Python package to manage LMS records from various vendors.

## Install

```bash
git clone https://github.com/illumidesk/lmsclient
cd lmsclient
pip install .
```

## Examples

In addition to the examples in the section below, the examples/ folder contains code examples for different end-to-end use-cases.

### Canvas LMS Client

1. Copy the `.env.example` file and create a new `.env` file with your `API_KEY` and `API_DOMAIN` values.

1. Initialize the `CanvasClient` class:

```python
from lmsclient.canvas import CanvasLmsClient

API_KEY = os.getenv('API_KEY')
API_DOMAIN = os.getenv('API_DOMAIN')

myclient1 = CanvasLmsClient(API_KEY, API_DOMAIN)
```

2. Fetch a list of courses for a Canvas user:

```python
courses = canvasild.fetch_courses()
for course in courses:
    print(f'Contents for course {course}')
```

3. Create courses in a separate Canvas instance (create a new client as instructed in step 1):

```python
import requests

url = "https://canvas.instructure.com/api/v1/accounts/:account_id/courses"
payload = {
            "course[id]": 4,
            "course[name]": "bizzbazz",
            "course[course_code]": "foobar",
        }
headers = {
  'Authorization': 'Bearer my-api-token',
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
```

4. Create a new assignment:

```python
import requests

url = "https://illumidesk.instructure.com/api/v1/courses/329/assignments"

payload={
    'assignment[name]': 'foobar3',
    'assignment[external_tool_tag_attributes]': '{"url": "https://flatiron-enterprise2.illumidesk.com/hub/lti/launch?foo=bar", "new_tab": True, "resource_link_id": "3722e75fb935a1f94f07e4ca027e5459263543d4", "external_data": "", "content_type": "ContextExternalTool", "content_id": 1305, "custom": None}',
    'assignment[points_possible]': '',
    'assignment[grading_type]': '',
    'assignment[due_at]': '',
headers = {
  'Authorization': 'Bearer my-api-token',
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


```

4. Update an assignment's external tool:

```python
import requests

url = "https://illumidesk.instructure.com/api/v1/courses/329/assignments"

payload={
    'assignment[name]': 'foobar3',
    'assignment[external_tool_tag_attributes]': '{"url": "https://flatiron-enterprise2.illumidesk.com/hub/lti/launch?foo=bar", "new_tab": True, "resource_link_id": "3722e75fb935a1f94f07e4ca027e5459263543d4", "external_data": "", "content_type": "ContextExternalTool", "content_id": 1305, "custom": None}',
    'assignment[points_possible]': '',
    'assignment[grading_type]': '',
    'assignment[due_at]': '',
headers = {
  'Authorization': 'Bearer my-api-token',
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)

```

## License

MIT
