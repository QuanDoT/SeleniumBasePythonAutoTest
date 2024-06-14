import datetime
from pathlib import Path

import pytest

from definitions import ROOT_DIR
from helpers.datetime_helper import get_month_name_full
from helpers.table_helper import TableHelper
from helpers.test_data_helper import read_test_data_from_csv
from page_object_models.locators.student_registration_form_page_locators import StudentRegistrationFormPageLocators
from page_object_models.student_registration_form_page import StudentRegistrationFormPage


class TestStudentRegistrationForm:
    @pytest.mark.parametrize("test_data", read_test_data_from_csv(
        Path(ROOT_DIR, 'files/test_data', 'student_form_valid_data.csv')))
    def test_student_register_with_valid_data_should_see_success_submission_dialog(self, test_data, sb):
        first_name = test_data['firstName']
        last_name = test_data['lastName']
        email = test_data['email']
        gender = test_data['gender']
        mobile_phone_number = test_data['mobilePhoneNumber']
        day = None if not test_data['dayOfBirth'] else int(test_data['dayOfBirth'])
        month = None if not test_data['monthOfBirth'] else int(test_data['monthOfBirth'])
        year = None if not test_data['yearOfBirth'] else int(test_data['yearOfBirth'])
        subjects = test_data['subjects'].split(", ")
        hobbies = test_data['hobbies'].split(", ")
        file_name = test_data['fileName']
        current_address = test_data['currentAddress']
        state = test_data['state']
        city = test_data['city']

        student_registration_form_page = StudentRegistrationFormPage(sb)
        (student_registration_form_page
         .go_to()
         .fill_first_name(first_name)
         .fill_last_name(last_name)
         .fill_email(email)
         .choose_gender(gender)
         .fill_mobile_phone_number(mobile_phone_number)
         .choose_date_of_birth(day=day, month=month, year=year)
         .input_subjects(*subjects)
         .choose_hobbies(*hobbies)
         .upload_picture_from_files(file_name)
         .input_current_address(current_address)
         .choose_state(state)
         .choose_city(city)
         .click_submit())

        sb.assert_element(StudentRegistrationFormPageLocators.THANK_YOU_FOR_SUBMITTING_DIALOG)

        actual_result = TableHelper(sb).get_table_body_texts_as_dict()

        expected_result = dict({
            'Student Name': f'{first_name} {last_name}',
            'Student Email': email,
            'Gender': gender,
            'Mobile': mobile_phone_number,
            'Date of Birth':
                f'{datetime.datetime(year, month, day).strftime('%d')} {get_month_name_full(month)},{year}',
            'Subjects': ', '.join(subject for subject in subjects),
            'Hobbies': ', '.join(hobby for hobby in hobbies),
            'Picture': file_name,
            'Address': current_address,
            'State and City': f'{state} {city}'
        })

        assert actual_result == expected_result

    @pytest.mark.parametrize("test_data", read_test_data_from_csv(
        Path(ROOT_DIR, 'files/test_data', 'student_form_invalid_data.csv')))
    def test_student_register_with_invalid_data_should_not_see_success_submission_dialog(self, test_data, sb):
        first_name = test_data['firstName']
        last_name = test_data['lastName']
        email = test_data['email']
        gender = test_data['gender']
        mobile_phone_number = test_data['mobilePhoneNumber']
        day = None if not test_data['dayOfBirth'] else int(test_data['dayOfBirth'])
        month = None if not test_data['monthOfBirth'] else int(test_data['monthOfBirth'])
        year = None if not test_data['yearOfBirth'] else int(test_data['yearOfBirth'])
        subjects = test_data['subjects'].split(", ")
        hobbies = test_data['hobbies'].split(", ")
        file_name = test_data['fileName']
        current_address = test_data['currentAddress']
        state = test_data['state']
        city = test_data['city']

        student_registration_form_page = StudentRegistrationFormPage(sb)
        (student_registration_form_page
         .go_to()
         .fill_first_name(first_name)
         .fill_last_name(last_name)
         .fill_email(email)
         .choose_gender(gender)
         .fill_mobile_phone_number(mobile_phone_number)
         .choose_date_of_birth(day=day, month=month, year=year)
         .input_subjects(*subjects)
         .choose_hobbies(*hobbies)
         .upload_picture_from_files(file_name)
         .input_current_address(current_address)
         .choose_state(state)
         .choose_city(city)
         .click_submit())

        sb.assert_element_not_visible(StudentRegistrationFormPageLocators.THANK_YOU_FOR_SUBMITTING_DIALOG)
