""" Testing read_student_file """

# pylint: disable=redefined-outer-name
from utils import read_student_file


def test_read_student_file(conftest):
    """ Test read_student_file """
    expectedoutput = [["delgrecoj", True, True, False, True]]
    assert read_student_file.read_student_file() == expectedoutput
