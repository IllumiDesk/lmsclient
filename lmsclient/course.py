import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class CourseException(Exception):
    """Canvas client exception
    """
    pass


class Course:
    """Assignment class
    """
    def __init__(self, *args):

        for x in args:
            self.x = x

        # course['name']: '',
        # course['course_code']: '',
        # course['start_at']: '',
        # course['end_at']: '',
        # course['license']: '',
        # course['is_public']: '',
        # course['is_public_to_auth_users']: '',
        # course['public_syllabus']: '',
        # course['public_syllabus_to_auth']: '',
        # course['public_description']: '',
        # course['allow_student_wiki_edits']: '',
        # course['allow_wiki_comments']: '',
        # course['allow_student_forum_attachments']: '',
        # course['open_enrollment']: '',
        # course['self_enrollment']: '',
        # course['restrict_enrollments_to_course_dates']: '',
        # course['term_id']: '',
        # course['sis_course_id']: '',
        # course['integration_id']: '',
        # course['hide_final_grades']: '',
        # course['apply_assignment_group_weights']: '',
        # course['time_zone']: '',
        # 'offer': '',
        # 'enroll_me': '',
        # course['default_view']: '',
        # course['syllabus_body']: '',
        # course['grading_standard_id']: '',
        # course['grade_passback_setting']: '',
        # course['course_format']: '',
        # 'enable_sis_reactivation': '',