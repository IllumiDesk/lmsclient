import attr
from cattr import unstructure
from lmsclient.utils import flatten_dict


@attr.s
class CourseCalendar:
    name = attr.ib()
    start_date = attr.ib()


@attr.s
class Course:
    id: int = attr.ib()
    name = attr.ib()
    calendar = attr.ib(validator=attr.validators.instance_of(CourseCalendar))


p = unstructure(
    Course(
        id=1,
        name="intro101",
        calendar=CourseCalendar(name="shreck", start_date="asdfasdf"),
    )
)

print(p)

print(flatten_dict(p))
