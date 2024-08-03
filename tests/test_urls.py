import pytest
from myao.errors import InvalidSubcategory, InvalidPage
from myao.parameters import Category, Filter, Order, Sorting, Subcategory
from myao.urls import Formatter
from myao.sites import NyaaSite, SukebeiSite
from typing import Set


FORMATTER = Formatter()


def test_set_valid_subcategory() -> None:
    for site in NyaaSite:
        FORMATTER.site = site
        _test_set_valid_subcategory(Category.get_nyaa_categories())
    for site in SukebeiSite:
        FORMATTER.site = site
        _test_set_valid_subcategory(Category.get_subekei_categories())


def _test_set_valid_subcategory(categories: Set[Category]) -> None:
    for category in categories:
        FORMATTER.category = category
        for subcategory in category.value.subcategories:
            FORMATTER.subcategory = subcategory


def test_set_invalid_subcategory() -> None:
    for site in NyaaSite:
        FORMATTER.site = site
        _test_set_invalid_subcategory(Category.get_nyaa_categories())
    for site in SukebeiSite:
        FORMATTER.site = site
        _test_set_invalid_subcategory(Category.get_subekei_categories())


def _test_set_invalid_subcategory(categories: Set[Category]) -> None:
    for category in categories:
        FORMATTER.category = category
        subcategories = set(Subcategory).difference(set(category.value.subcategories.keys()))
        for subcategory in subcategories:
            with pytest.raises(InvalidSubcategory):
                FORMATTER.subcategory = subcategory


def test_set_category_at_none() -> None:
    FORMATTER.category = None
    assert FORMATTER.category is Category.ALL_CATEGORIES


def test_set_filter_at_none() -> None:
    FORMATTER.filter = None
    assert FORMATTER.filter is Filter.NO_FILTER


def test_set_order_at_none() -> None:
    FORMATTER.order = None
    assert FORMATTER.order is Order.DESCENDANT


def test_set_sorting_at_none() -> None:
    FORMATTER.sorting = None
    assert FORMATTER.sorting is Sorting.ID


def test_set_invalid_page() -> None:
    with pytest.raises(InvalidPage):
        FORMATTER.page = -1
