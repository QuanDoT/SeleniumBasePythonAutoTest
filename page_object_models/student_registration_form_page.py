import datetime
from pathlib import Path

import allure
from selenium.webdriver import Keys

from constants.enums.genders_enum import GendersEnum
from constants.enums.hobbies_enum import HobbiesEnum
from definitions import ROOT_DIR
from helpers.datetime_helper import get_day_of_week, get_date_suffix, get_month_name_full
from page_object_models.locators.student_registration_form_page_locators import StudentRegistrationFormPageLocators


class StudentRegistrationFormPage:
    def __init__(self, sb):
        self.__sb = sb

    @allure.step('Go to Student Registration Form page')
    def go_to(self):
        self.__sb.open('https://demoqa.com/automation-practice-form')

        return self

    @allure.step('Fill First Name')
    def fill_first_name(self, value: str):
        self.__sb.type(StudentRegistrationFormPageLocators.FIRST_NAME_INPUT, value)

        return self

    @allure.step('Fill Last Name')
    def fill_last_name(self, value: str):
        self.__sb.type(StudentRegistrationFormPageLocators.LAST_NAME_INPUT, value)

        return self

    @allure.step('Fill Email')
    def fill_email(self, value: str):
        self.__sb.type(StudentRegistrationFormPageLocators.EMAIL_INPUT, value)

        return self

    @allure.step('Choose Gender')
    def choose_gender(self, value: str):
        if value == GendersEnum.MALE.value:
            self.__sb.click(StudentRegistrationFormPageLocators.MALE_RADIO_BUTTON)
        elif value == GendersEnum.FEMALE.value:
            self.__sb.click(StudentRegistrationFormPageLocators.FEMALE_RADIO_BUTTON)
        elif value == GendersEnum.OTHER.value:
            self.__sb.click(StudentRegistrationFormPageLocators.OTHER_RADIO_BUTTON)

        return self

    @allure.step('Fill Mobile Phone number')
    def fill_mobile_phone_number(self, value: str):
        self.__sb.type(StudentRegistrationFormPageLocators.MOBILE_NUMBER_INPUT, value)

        return self

    @allure.step('Choose Date of Birth by clicking')
    def choose_date_of_birth(self, day: int, month: int, year: int):
        self.__sb.click(StudentRegistrationFormPageLocators.DATE_OF_BIRTH_INPUT)

        if month is not None:
            month_name_full = get_month_name_full(month)
            self.__sb.select_option_by_text(StudentRegistrationFormPageLocators.DATE_PICKER_MONTH_SELECT,
                                            month_name_full)

        if year is not None:
            self.__sb.select_option_by_text(StudentRegistrationFormPageLocators.DATE_PICKER_YEAR_SELECT, str(year))

        if day is not None:
            datetime_dto = datetime.datetime(year=year, month=month, day=day)

            self.__sb.click(StudentRegistrationFormPageLocators.DATE_PICKER_DAY_OPTION.format(
                f'Choose {get_day_of_week(datetime_dto)}, {get_month_name_full(month)} '
                f'{day}{get_date_suffix(day)}, {year}'))

        return self

    @allure.step('Choose Subjects')
    def input_subjects(self, *args: str):
        for subject in args:
            self.__sb.send_keys(StudentRegistrationFormPageLocators.SUBJECTS_INPUT, subject)
            self.__sb.press_keys(StudentRegistrationFormPageLocators.SUBJECTS_INPUT, Keys.ENTER)

        return self

    @allure.step('Choose Hobbies')
    def choose_hobbies(self, *args: str):
        for hobby in args:
            if hobby == HobbiesEnum.SPORTS.value:
                self.__sb.click(StudentRegistrationFormPageLocators.HOBBIES_SPORTS_CHECKBOX)
            elif hobby == HobbiesEnum.READING.value:
                self.__sb.click(StudentRegistrationFormPageLocators.HOBBIES_READING_CHECKBOX)
            elif hobby == HobbiesEnum.MUSIC.value:
                self.__sb.click(StudentRegistrationFormPageLocators.HOBBIES_MUSIC_CHECKBOX)

        return self

    @allure.step('Upload file')
    def upload_picture_from_files(self, file_path: str):
        if file_path and not file_path.isspace():
            self.__sb.choose_file(StudentRegistrationFormPageLocators.FILE_UPLOAD_BUTTON,
                                  Path(ROOT_DIR, 'files', file_path))

        return self

    @allure.step('Fill Current Address')
    def input_current_address(self, value: str):
        self.__sb.type(StudentRegistrationFormPageLocators.CURRENT_ADDRESS_INPUT, value)

        return self

    @allure.step('Choose State')
    def choose_state(self, state: str):
        if state and not state.isspace():
            self.__sb.click(StudentRegistrationFormPageLocators.STATE_SELECT)
            self.__sb.click(StudentRegistrationFormPageLocators.STATE_OPTION.format(state))

        return self

    @allure.step('Choose City')
    def choose_city(self, city: str):
        if city and not city.isspace():
            self.__sb.click(StudentRegistrationFormPageLocators.CITY_SELECT)
            self.__sb.click(StudentRegistrationFormPageLocators.CITY_OPTION.format(city))

        return self

    @allure.step('Click Submit form')
    def click_submit(self):
        self.__sb.click(StudentRegistrationFormPageLocators.SUBMIT_BUTTON)

        return self
