import os

from prodex import process_xml


def test_product_without_parts():
    assert process_xml(os.path.join(os.path.os.getcwd(),'test_data', 'without_parts.xml')) == [{'name': 'Uhlíková tyčka 0.6mm (1m)'}]


def test_product_with_parts():
    assert process_xml(os.path.join(os.path.curdir, 'test_data', 'with_parts.xml')) == [{'name': 'Pult pro ST16 / ST24 uhlík', 'parts': ['ASTRA popruh vysílače jednoduchý']}]
