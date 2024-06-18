import datetime
from pathlib import Path

import pytest

from definitions import ROOT_DIR
from helpers.datetime_helper import get_month_name_full
from helpers.test_data_helper import read_test_data_from_csv
from page_object_models.common_components.html_table import HtmlTable
from page_object_models.locators.student_registration_form_page_locators import StudentRegistrationFormPageLocators
from page_object_models.student_registration_form_page import StudentRegistrationFormPage


class TestStudentRegistrationForm:
    @pytest.mark.parametrize("test_data", read_test_data_from_csv(
        Path(ROOT_DIR, 'files/test_data', 'student_form_valid_data.csv')))
    def test_student_register_with_valid_data_should_see_success_submission_dialog(self, test_data, sb):
        data = map_test_data(test_data)

        student_registration_form_page = StudentRegistrationFormPage(sb)
        (student_registration_form_page
         .go_to()
         .fill_first_name(data.first_name)
         .fill_last_name(data.last_name)
         .fill_email(data.email)
         .choose_gender(data.gender)
         .fill_mobile_phone_number(data.mobile_phone_number)
         .choose_date_of_birth(day=data.day, month=data.month, year=data.year)
         .input_subjects(*data.subjects)
         .choose_hobbies(*data.hobbies)
         .upload_picture_from_files(data.file_name)
         .input_current_address(data.current_address)
         .choose_state(data.state)
         .choose_city(data.city)
         .click_submit())

        sb.assert_element(StudentRegistrationFormPageLocators.THANK_YOU_FOR_SUBMITTING_DIALOG)

        actual_result = HtmlTable(sb).wait_for_table_exist().get_table_body_texts_as_dict()

        expected_result = create_expected_form_result(data)

        assert actual_result == expected_result

    @pytest.mark.parametrize("test_data", read_test_data_from_csv(
        Path(ROOT_DIR, 'files/test_data', 'student_form_invalid_data.csv')))
    def test_student_register_with_invalid_data_should_not_see_success_submission_dialog(self, test_data, sb):
        data = map_test_data(test_data)

        student_registration_form_page = StudentRegistrationFormPage(sb)
        (student_registration_form_page
         .go_to()
         .fill_first_name(data.first_name)
         .fill_last_name(data.last_name)
         .fill_email(data.email)
         .choose_gender(data.gender)
         .fill_mobile_phone_number(data.mobile_phone_number)
         .choose_date_of_birth(day=data.day, month=data.month, year=data.year)
         .input_subjects(*data.subjects)
         .choose_hobbies(*data.hobbies)
         .upload_picture_from_files(data.file_name)
         .input_current_address(data.current_address)
         .choose_state(data.state)
         .choose_city(data.city)
         .click_submit())

        sb.assert_element_not_visible(StudentRegistrationFormPageLocators.THANK_YOU_FOR_SUBMITTING_DIALOG)


class FormTestData:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile_phone_number: str
    day: int | None
    month: int | None
    year: int | None
    subjects: str
    hobbies: str
    file_name: str
    current_address: str
    state: str
    city: str

    def __init__(self, first_name, last_name, email, gender, mobile_phone_number, day, month, year, subjects, hobbies,
                 file_name, current_address, state, city):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.mobile_phone_number = mobile_phone_number
        self.day = day
        self.month = month
        self.year = year
        self.subjects = subjects
        self.hobbies = hobbies
        self.file_name = file_name
        self.current_address = current_address
        self.state = state
        self.city = city


def create_expected_form_result(data: FormTestData):
    if not data.day or not data.month or not data.year:
        today = datetime.datetime.today()
        expected_dob = f'{today.strftime('%d')} {get_month_name_full(today.month)},{today.year}'
    else:
        expected_dob = (f'{datetime.datetime(data.year, data.month, data.day).strftime('%d')}'
                        f' {get_month_name_full(data.month)},{data.year}')

    if not data.state or not data.city:
        expected_state_and_city = ''
    else:
        expected_state_and_city = f'{data.state} {data.city}'

    return dict({
        'Student Name': f'{data.first_name} {data.last_name}',
        'Student Email': data.email,
        'Gender': data.gender,
        'Mobile': data.mobile_phone_number,
        'Date of Birth': expected_dob,
        'Subjects': ', '.join(subject for subject in data.subjects),
        'Hobbies': ', '.join(hobby for hobby in data.hobbies),
        'Picture': data.file_name,
        'Address': data.current_address,
        'State and City': expected_state_and_city
    })


def map_test_data(test_data):
    return FormTestData(
        first_name=test_data['firstName'],
        last_name=test_data['lastName'],
        email=test_data['email'],
        gender=test_data['gender'],
        mobile_phone_number=test_data['mobilePhoneNumber'],
        day=None if not test_data['dayOfBirth'] else int(test_data['dayOfBirth']),
        month=None if not test_data['monthOfBirth'] else int(test_data['monthOfBirth']),
        year=None if not test_data['yearOfBirth'] else int(test_data['yearOfBirth']),
        subjects=test_data['subjects'].split(", "),
        hobbies=test_data['hobbies'].split(", "),
        file_name=test_data['fileName'],
        current_address=test_data['currentAddress'],
        state=test_data['state'],
        city=test_data['city']
    )
