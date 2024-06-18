from page_object_models.locators.common_components.confirmation_dialog_locators import ConfirmationDialogLocators


class ConfirmationDialog:
    def __init__(self, sb):
        self.__sb = sb

    def click_confirm(self):
        self.__sb.click(ConfirmationDialogLocators.OK_BUTTON)

    def click_cancel(self):
        self.__sb.click(ConfirmationDialogLocators.CANCEL_BUTTON)