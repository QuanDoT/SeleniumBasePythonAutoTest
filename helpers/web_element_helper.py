def get_text_from_elements(web_elements):
    for element in web_elements:
        yield element.text


