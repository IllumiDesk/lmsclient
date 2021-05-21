import logging
from typing import Optional

import attr

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class CourseException(Exception):
    """Canvas client exception"""

    pass


@attr.define
class CourseCalendar:
    ics: str = attr.ib()


@attr.define
class CourseEnrollment:
    type: str = attr.ib()
    role: str = attr.ib()
    role_id: int = attr.ib()
    user_id: int = attr.ib()
    enrollment_state: str = attr.ib()
    limit_privileges_to_course_section: bool = attr.ib()


@attr.define
class Course:
    id: int = attr.ib()
    name: str = attr.ib()
    account_id: int = attr.ib()
    uuid: str = attr.ib()
    start_at: str = attr.ib()
    grading_standard_id: str = attr.ib()
    is_public: bool = attr.ib()
    created_at: str = attr.ib()
    course_code: str = attr.ib()
    default_view: str = attr.ib()
    root_account_id: int = attr.ib()
    enrollment_term_id: int = attr.ib()
    license: str = attr.ib()
    grade_passback_setting: str = attr.ib()
    end_at: str = attr.ib()
    public_syllabus: str = attr.ib()
    public_syllabus_to_auth: str = attr.ib()
    storage_quota_mb: int = attr.ib()
    is_public_to_auth_users: bool = attr.ib()
    homeroom_course: bool = attr.ib()
    course_color: str = attr.ib()
    apply_assignment_group_weights: str = attr.ib()
    calendar: CourseCalendar = attr.ib(
        validator=attr.validators.instance_of(CourseCalendar)
    )
    time_zone: bool = attr.ib()
    blueprint: bool = attr.ib()
    template: bool = attr.ib()
    sis_course_id: int = attr.ib()
    sis_import_id: int = attr.ib()
    integration_id: int = attr.ib()
    enrollments: Optional[CourseEnrollment] = attr.ib(
        validator=attr.validators.instance_of(CourseEnrollment)
    )
    workflow_state: str = attr.ib()
    restrict_enrollments_to_course_dates: bool = attr.ib()
    overridden_course_visibility: str = attr.ib()
