# LMS Client API

Python package to manage LMS records from various vendors.

## Install

    pip install lmsclient

## Examples

First, initialize the `CanvasLmsClient` class:

```python
from lmsclient.canvas import CanvasLmsClient

api_key = "your Canvas API Key"
api_url = "https://illumidesk.instructure.com"
course_id = "123"
api_key = "illumidesk.instructure.com"

client = CanvasLmsClient(api_key, api_url, course_id, instructure_domain)
```

### Fetch assignments for a course



