import logging
import json

import requests

from typing import List

from .assignment import Assignment
from .course import Course
from .external_tool import ExternalTool


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class CanvasClientException(Exception):
    """Canvas client exception
    """
    pass


class CanvasClient:
    """Canvas Python client"""
    def __init__(self, api_key: str, instructure_domain: str, is_debug: bool = True):
        """
        Canvas client class.
        
        Args:
          api_key: the Canvas API Key
          instructure_domain: the Canvas LMS domain
          is_debug: if true, logging is set to debug
        
        Raises:
          ConfigException if the kubectl python client does not have a valid configuration set.
        """
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
        }
        self.instructure_domain = instructure_domain
        self.api_url = f'https://{self.instructure_domain}/api/v1'
        self.is_debug = is_debug

    def fetch_account(self, account_id: str) -> json:
        """Fetch an account for a Canvas LMS instance

        Returns:
            json: an account object
        """
        url = f'{self.instructure_domain}/accounts/{account_id}'
        response = requests.get(
            url,
            headers=self.headers,)

        return response.json()

    def fetch_accounts(self) -> List:
        """Fetch the accounts for a Canvas LMS instance

        Returns:
            List: a list of accounts
        """
        url = f'{self.instructure_domain}/accounts'
        response = requests.get(
            url,
            headers=self.headers,)

        return response.json()
    
    def fetch_courses(self) -> List:
        """Fetch a list of courses from a Canvas LMS instance
        
        Returns:
          All course objects for a Canvas instance as a list of JSONs.
        """
        url = f'{self.api_url}/courses'
        response = requests.get(
            url,
            headers=self.headers,)

        return response.json()

    def fetch_course(self, course_id: str) -> json:
        """Fetch course by id from a Canvas LMS instance
        
        Returns:
          All course objects for a Canvas instance as a list of JSONs.
        """
        url = f'{self.api_url}/courses/{course_id}'
        response = requests.get(
            url,
            headers=self.headers,)
        
        return response.json()

    def create_course(self, account_id: str, course: Course) -> json:
        """Create a course in a Canvas instance account

        Args:
            account_id(str): the account id
            course (json): the course to create
        
        Returns:
            json: the created course
        """
        url = f'{self.api_url}/accounts/{account_id}/courses'

        payload={
            course['name']: '',
            course['course_code']: '',
            course['start_at']: '',
            course['end_at']: '',
            course['license']: '',
            course['is_public']: '',
            course['is_public_to_auth_users']: '',
            course['public_syllabus']: '',
            course['public_syllabus_to_auth']: '',
            course['public_description']: '',
            course['allow_student_wiki_edits']: '',
            course['allow_wiki_comments']: '',
            course['allow_student_forum_attachments']: '',
            course['open_enrollment']: '',
            course['self_enrollment']: '',
            course['restrict_enrollments_to_course_dates']: '',
            course['term_id']: '',
            course['sis_course_id']: '',
            course['integration_id']: '',
            course['hide_final_grades']: '',
            course['apply_assignment_group_weights']: '',
            course['time_zone']: '',
            'offer': '',
            'enroll_me': '',
            course['default_view']: '',
            course['syllabus_body']: '',
            course['grading_standard_id']: '',
            course['grade_passback_setting']: '',
            course['course_format']: '',
            'enable_sis_reactivation': '',
        }

        response = requests.post(url, headers=self.headers, data=payload)
        return response.json()

    def update_course(self, account_id: str, course_id:str) -> json:
        """Create a course in a Canvas instance account

        Args:
            account_id(str): the account id
            course (json): the course to create
        
        Returns:
            json: the created course
        """
        course = self.fetch_course(course_id)
        url = f'{self.api_url}/accounts/{account_id}/courses'

        payload={
            course['name']: '',
            course['course_code']: '',
            course['start_at']: '',
            course['end_at']: '',
            course['license']: '',
            course['is_public']: '',
            course['is_public_to_auth_users']: '',
            course['public_syllabus']: '',
            course['public_syllabus_to_auth']: '',
            course['public_description']: '',
            course['allow_student_wiki_edits']: '',
            course['allow_wiki_comments']: '',
            course['allow_student_forum_attachments']: '',
            course['open_enrollment']: '',
            course['self_enrollment']: '',
            course['restrict_enrollments_to_course_dates']: '',
            course['term_id']: '',
            course['sis_course_id']: '',
            course['integration_id']: '',
            course['hide_final_grades']: '',
            course['apply_assignment_group_weights']: '',
            course['time_zone']: '',
            'offer': '',
            'enroll_me': '',
            course['default_view']: '',
            course['syllabus_body']: '',
            course['grading_standard_id']: '',
            course['grade_passback_setting']: '',
            course['course_format']: '',
            'enable_sis_reactivation': '',
        }

        response = requests.put(url, headers=self.headers, data=payload)
        return response.json()

    def create_course(self, *args) -> List:
        result = 0
        # Iterating over the Python args tuple
        for x in args:
            result += x
        return result

    def fetch_assignments(self, course_id: str)  -> List:
        """Fetch a list of assignments for a course
        
        Returns:
            List: All assignment objects for a course as a list of JSONs.
        """
        url = f'{self.api_url}/courses/{course_id}/assignments'
        response = requests.get(
            url,
            headers=self.headers,)
        
        return response.json()

    def fetch_assignment(self, course_id: str, assignment_id: str) -> json:
        """Fetch assignment for a course by id
        
        Args:
          assignment_id(str): fetch an assignment by id for a course
        
        Returns:
          json: Assignment object as JSON
        """
        url = f'{self.api_url}/courses/{course_id}/assignments/{assignment_id}'
        response = requests.get(
            url,
            headers=self.headers,)
        
        return response.json()

    def create_assignment(self, course_id:str, assignment: json) -> json:
        """Create an assignment for a give course.

        Args:
            course_id (str): the course id
            assignment (json): the assignment represented in json

        Returns:
            json: the created assignment returned as JSON
        """
        url = f'{self.api_url}/courses/{course_id}/assignments'
        response = requests.put(url,
            headers=self.headers,
            json=assignment.json())
        
        return response.json()

    def fetch_external_tools_by_course(self, course_id: str) -> json:
        """Fetch a list of external tools by course id.

        Args:
            course_id (str): the course id

        Returns:
            json: the external tool object represented as json
        """
        url = f'{self.api_url}/courses/{course_id}/external_tools'
        response = requests.get(url,
            headers=self.headers)
        
        return response.json()


    def fetch_external_tool_by_course(self, course_id:str, external_tool_id: str) -> json:
        """Fetch an external tool by id.

        Args:
            course_id (str): the course id
            external_tool_id (str): the external tool id

        Returns:
            json: the external tool object represented as json
        """
        url = f'{self.api_url}/courses/{course_id}/external_tools/{external_tool_id}'
        response = requests.get(url,
            headers=self.headers)
        
        return response.json()

    def fetch_external_tools_by_account(self, account_id: str) -> json:
        """Fetch a list of external tools by account id.

        Args:
            account_id (str): the account id

        Returns:
            json: the external tool object represented as json
        """
        url = f'{self.api_url}/accounts/{account_id}/external_tools'
        response = requests.get(url,
            headers=self.headers)
        
        return response.json()

    def fetch_external_tool_by_account(self, account_id:str, external_tool_id: str) -> json:
        """Fetch an external tool by id associated to an account.

        Args:
            account_id (str): the course id
            external_tool_id (str): the external tool id

        Returns:
            json: the external tool object represented as json
        """
        url = f'{self.api_url}/accounts/{account_id}/external_tools/{external_tool_id}'
        response = requests.get(url,
            headers=self.headers)
        
        return response.json()

    def create_external_tool_by_course(self, course_id:str) -> json:
        """Create an external tool for a course

        Args:
            course_id (str): the course id

        Returns:
            json: the external tool object as json
        """
        url = f'{self.api_url}/courses/{course_id}/external_tools'
        response = requests.post(
            url,
            headers=self.headers,)
        
        return response.json()

    def update_external_tool_by_course(self, course_id:str) -> json:
        """Update an external tool for a course

        Args:
            course_id (str): the course id

        Returns:
            json: the external tool object as json
        """
        url = f'{self.api_url}/courses/{course_id}/external_tools'
        response = requests.put(
            url,
            headers=self.headers,)
        
        return response.json()

    def create_external_tool_by_account(self, account_id:str) -> json:
        """Create an external tool for a account

        Args:
            account_id (str): the account id

        Returns:
            json: the external tool object as json
        """
        url = f'{self.api_url}/accounts/{account_id}/external_tools'
        response = requests.post(
            url,
            headers=self.headers,)
        
        return response.json()

    def update_external_tool_by_account(self, account_id:str) -> json:
        """Update an external tool for a account

        Args:
            account_id (str): the account id

        Returns:
            json: the external tool object as json
        """
        url = f'{self.api_url}/accounts/{account_id}/external_tools'
        response = requests.put(
            url,
            headers=self.headers,)
        
        return response.json()

    def update_assignment(self, course_id:str, assignment_id: str, assignment: dict) -> json:
        """Update an assignment in a course
        
        Args:
            course_id (str): the course that has the assignment
            assignment_id (str): the assignment id to update
            assignment (Assignment): the updated assignment
        
        Returns:
            json: Updated assignment object as JSON
        """
        url = f'{self.api_url}/courses/{course_id}/assignments/{assignment_id}'
        response = requests.put(url,
            headers=self.headers,
            data=assignment)
        
        return response.json()
