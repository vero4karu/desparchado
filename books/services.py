import logging

from django.conf import settings

from .goodreads_client import GoodreadsClient
from .taganga_client import TagangaClient
from desparchado.exceptions import RequestFailureException
from desparchado.exceptions import UnknownResultException


logger = logging.getLogger(__name__)


def get_goodreads_client(timeout_secs=10):
    return GoodreadsClient(
        developer_key=settings.GOODREADS_API_KEY,
        timeout_secs=timeout_secs,
    )


def get_taganga_client(timeout_secs=10):
    return TagangaClient(
        base_url=settings.TAGANGA_BASE_URL,
        auth_token=settings.TAGANGA_AUTH_TOKEN,
        timeout_secs=timeout_secs,
    )


def goodreads_search_book(search_string):
    goodreads_client = get_goodreads_client(timeout_secs=10)
    try:
        response_data = goodreads_client.search_book(search_string)
    except RequestFailureException:
        return None
    except UnknownResultException:
        return None

    return response_data


def goodreads_get_book_info(book_isbn):
    goodreads_client = get_goodreads_client(timeout_secs=10)
    try:
        root = goodreads_client.get_book_info(book_isbn)
    except (RequestFailureException, UnknownResultException):
        return None

    book_data = root.find('book')

    return dict(
        title=book_data.find('title').text,
        description=book_data.find('description').text,
        image_url=book_data.find('image_url').text,
        url=book_data.find('url').text,
        average_rating=book_data.find('average_rating').text,
        ratings_count=book_data.find('ratings_count').text,
    )


def taganga_get_book_prices(book_isbn):
    taganga_client = get_taganga_client()

    try:
        prices_list = taganga_client.get_book_prices(book_isbn)
    except (RequestFailureException, UnknownResultException) as e:
        return []

    if type(prices_list) is not list:
        return []

    return prices_list

