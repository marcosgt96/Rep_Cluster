import os
import sqlite3
import pytest
from db import DB_PATH, init_db
from models import (
    add_product,
    list_products,
    update_product_quantity,
    add_seller,
    list_sellers,
    update_seller_name,
    delete_seller,
    record_sale,
    get_full_report,
)


def setup_function(fn):
    # delete db before each test
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    init_db()


def test_product_lifecycle():
    add_product('Banana', 'Frutas', 'kg', 1.0, 2.0, 5)
    prods = list_products()
    assert len(prods) == 1
    pid = prods[0][0]
    assert update_product_quantity(pid, 3)
    assert list_products()[0][6] == 8
    assert not update_product_quantity(pid, -100)


def test_seller_and_sale():
    add_seller('Joao')
    sellers = list_sellers()
    assert sellers and sellers[0][1] == 'Joao'
    pid = add_product('Laranja', 'Frutas', 'kg', 1, 2, 10) or list_products()[0][0]
    sid = sellers[0][0]
    sale_id = record_sale(sid, [(1, 2)])
    assert sale_id is not None
    rpt = get_full_report()
    assert any(r[0] == 'sale' for r in rpt)


def test_delete_seller():
    add_seller('Maria')
    sellers = list_sellers()
    assert sellers and sellers[0][1] == 'Maria'
    sid = sellers[0][0]
    # deleting with no sales should work
    assert delete_seller(sid)
    assert not list_sellers()

    # add again and record a sale
    add_seller('Maria')
    sellers = list_sellers()
    sid = sellers[0][0]
    pid = add_product('Pera', 'Frutas', 'kg', 1, 2, 5) or list_products()[0][0]
    sale_id = record_sale(sid, [(pid, 1)])
    assert sale_id is not None
    # now deletion should fail
    assert not delete_seller(sid)
    assert list_sellers()

    # test renaming
    sellers = list_sellers()
    sid = sellers[0][0]
    assert update_seller_name(sid, 'Maria Silva')
    assert list_sellers()[0][1] == 'Maria Silva'
    # duplicate-name attempt should fail
    add_seller('Joao')
    # find Joao's id explicitly (list sorted by name)
    sellers = list_sellers()
    sid2 = next(s[0] for s in sellers if s[1] == 'Joao')
    assert not update_seller_name(sid2, 'Maria Silva')
