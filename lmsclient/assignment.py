import logging
from enum import Enum
from typing import Dict
from typing import List

import attr

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class AssignmentException(Exception):
    """Canvas client exception"""

    pass


class AssignmentSubmissionTypes(Enum):
    """Assignment submission types"""

    pass


@attr.define
class AssignmentExternalToolTagAttributes:
    """Assignment's external tool tag attributes class"""

    url = attr.ib()
    new_tab = attr.ib(validator=attr.validators.instance_of(bool), default=True)
    resource_link_id = attr.ib()
    external_data = attr.ib()
    content_type = attr.ib()
    content_id = attr.ib(validator=attr.validators.instance_of(int))
    custom = attr.ib()


@attr.define
class Assignment:
    """Assignment class"""

    id = attr.ib(validator=attr.validators.instance_of(int))
    name = attr.ib()
    position = attr.ib()
    submission_types: List[AssignmentSubmissionTypes] = attr.ib()
    allowed_extensions = attr.ib()
    turnitin_enabled = attr.ib()
    vericite_enabled = attr.ib()
    turnitin_settings = attr.ib()
    integration_data = attr.ib()
    integration_id = attr.ib()
    peer_reviews = attr.ib()
    automatic_peer_reviews = attr.ib()
    notify_of_update = attr.ib()
    group_category_id = attr.ib()
    grade_group_students_individually = attr.ib()
    external_tool_tag_attributes: Dict = attr.ib()
    points_possible = attr.ib()
    grading_type = attr.ib()
    due_at = attr.ib()
    lock_at = attr.ib()
    unlock_at = attr.ib()
    description = attr.ib()
    assignment_group_id = attr.ib()
    assignment_overrides = attr.ib()
    only_visible_to_overrides = attr.ib()
    published = attr.ib()
    grading_standard_id = attr.ib()
    omit_from_final_grade = attr.ib()
    quiz_lti = attr.ib()
    moderated_grading = attr.ib()
    grader_count = attr.ib()
    final_grader_id = attr.ib()
    grader_comments_visible_to_graders = attr.ib()
    graders_anonymous_to_graders = attr.ib()
    graders_names_visible_to_final_grader = attr.ib()
    anonymous_grading = attr.ib()
    allowed_attempts = attr.ib()
