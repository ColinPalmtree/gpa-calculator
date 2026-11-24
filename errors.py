# errors.py
# our own exception types so we can tell what actually went wrong.
# they all come from GPAError so main can catch all of them at once


class GPAError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class InvalidGradeErr(GPAError):
    pass


class InvalidCreditsErr(GPAError):
    pass


class DuplicateCourseErr(GPAError):
    pass


class DuplicateSemesterErr(GPAError):
    pass


class CourseNotFoundErr(GPAError):
    pass


class SemesterNotFoundErr(GPAError):
    pass


# for when the save file is messed up
class SaveFileErr(GPAError):
    pass
