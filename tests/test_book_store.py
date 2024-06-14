import pytest

from page_object_models.book_store_page import BookStorePage


class TestBookStore:
    @pytest.mark.parametrize('keyword', ['design', 'Design'])
    def test_search_for_book_should_see_all_relevant_results(self, sb, keyword):
        book_store_page = BookStorePage(sb)
        (book_store_page
         .go_to()
         .search_for_book(keyword))

        book_titles = book_store_page.get_book_titles()

        for title in book_titles:
            assert keyword.lower() in title.lower()
