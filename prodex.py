import os
import tempfile
import typing
import xml.etree.ElementTree as ET
import zipfile

import requests as requests


def download_unzip_file(folder_path: str, zip_url: str) -> str:
    response = requests.get(zip_url)

    zip_path = os.path.join(folder_path, 'downloaded.zip')
    with open(zip_path, 'wb') as temp_zip:
        temp_zip.write(response.content)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(folder_path)
        if len(zip_ref.namelist()) == 0:
            raise ValueError('Archive is empty')
        if len(zip_ref.namelist()) > 1:
            raise ValueError('Archive contains multiple files')
        return os.path.join(folder_path, zip_ref.namelist()[0])


def process_xml(xml_file_path: str) -> typing.List[typing.Dict[str, str | typing.List[str]]]:
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    results = []
    for product in root.findall('./items/item'):
        name = product.get('name')
        data = {}
        if name:
            data['name'] = name
        else:
            ValueError('Item does not have a name')
        parts = [part.get('name') for part in product.findall('parts/part/item')]  # do we want to filter out non replacement part types?
        if parts:
            data['parts'] = parts
        results.append(data)
    return results


if __name__ == '__main__':
    url = 'https://www.retailys.cz/wp-content/uploads/astra_export_xml.zip'
    with tempfile.TemporaryDirectory() as tmp_dir:
        file_path = download_unzip_file(tmp_dir, url)
        results = process_xml(file_path)
        print('1 Number of products: ', len(results))
        print('====================')
        print('2 Current products:')
        for product in results:
            print('  Product name: ', product['name'])
        print('====================')
        print('3 Additional parts')
        for product in results:
            if product.get('parts'):
                print('  Product name: ', product['name'])
                for part in product['parts']:
                    print('    Part name: ', part)