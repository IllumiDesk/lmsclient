import os
import sys

from setuptools import find_packages
from setuptools import setup

v = sys.version_info
if v[:2] < (3, 6):
    error = "ERROR: lmsclient requires Python version 3.6 or above."
    print(error, file=sys.stderr)
    sys.exit(1)

shell = False
if os.name in ("nt", "dos"):
    shell = True
    warning = "WARNING: Windows is not officially supported"
    print(warning, file=sys.stderr)

# Get the current package version.
here = os.path.abspath(os.path.dirname(__file__))
version_ns = {}
with open(os.path.join("_version.py")) as f:
    exec(f.read(), {}, version_ns)

setup(
    name="lmsclient",
    version=version_ns["__version__"],
    description="IllumiDesk Learning Management System client package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/illumidesk/lmsclient",
    author="The IllumiDesk Team",
    author_email="hello@illumidesk.com",
    license="MIT",
    packages=find_packages(exclude="./tests"),
    install_requires=[
        "canvasapi==2.2.0",
        "flask==1.1.2",
        "flask-sqlalchemy==2.5.1",
        "gunicorn==20.0.4",
    ],  # noqa: E231
    package_data={
        "": ["*.html"],
    },  # noqa: E231
)
