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

1. Initialize the `CanvasClient` class:

```python
from lmsclient.canvas import CanvasLmsClient

api_key = "canvas-api-key"
instructure_domain = "illumidesk.instructure.com"

client = CanvasLmsClient(api_key, instructure_domain)
```

2. Fetch a list of courses for a Canvas instance:

```bash

```

3. Create courses in a separate Canvas instance:

```bash

```

4. Create a new assignment:

```bash

```

4. Update an assignment's external tool:

```bash

```

5. Migrate courses from one Canvas instance to another:

```bash

```

## License

MIT
