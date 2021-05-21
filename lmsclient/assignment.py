import logging

import attr

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class AssignmentException(Exception):
    """Canvas client exception"""

    pass


@attr.s
class Assignment:
    """Assignment class"""

    id = attr.ib(default="")
    name = attr.ib(default="")
    position = attr.ib(default="")
    submission_types = attr.ib(default="")
    allowed_extensions = attr.ib(default="")
    turnitin_enabled = attr.ib(default="")
    vericite_enabled = attr.ib(default="")
    turnitin_settings = attr.ib(default="")
    integration_data = attr.ib(default="")
    integration_id = attr.ib(default="")
    peer_reviews = attr.ib(default="")
    automatic_peer_reviews = attr.ib(default="")
    notify_of_update = attr.ib(default="")
    group_category_id = attr.ib(default="")
    grade_group_students_individually = attr.ib(default="")
    external_tool_tag_attributes = attr.ib(default="")
    points_possible = attr.ib(default="")
    grading_type = attr.ib(default="")
    due_at = attr.ib(default="")
    lock_at = attr.ib(default="")
    unlock_at = attr.ib(default="")
    description = attr.ib(default="")
    assignment_group_id = attr.ib(default="")
    assignment_overrides = attr.ib(default="")
    only_visible_to_overrides = attr.ib(default="")
    published = attr.ib(default="")
    grading_standard_id = attr.ib(default="")
    omit_from_final_grade = attr.ib(default="")
    quiz_lti = attr.ib(default="")
    moderated_grading = attr.ib(default="")
    grader_count = attr.ib(default="")
    final_grader_id = attr.ib(default="")
    grader_comments_visible_to_graders = attr.ib(default="")
    graders_anonymous_to_graders = attr.ib(default="")
    graders_names_visible_to_final_grader = attr.ib(default="")
    anonymous_grading = attr.ib(default="")
    allowed_attempts = attr.ib(default="")
