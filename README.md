# ProdEx - Product Data Extractor

**ProdEx** is a Python tool that works with a data ins astra format. It lets you easily access product names and related spare parts.

## Features
- Download & Decompress: Efficiently fetches ZIP archives encompassing XML and unravels them for streamlined processing.
- Product Analysis:
  - Compute the total number of products.
  - Enumerate all product designations.
  - Retrieve linked spare parts for each item (provided they're available).

## Prerequisites
- Python 3.10+    
- Access to internet (for fetching ZIP data)

## Installation & Setup
Clone the repository:

    git clone https://github.com/stekot/prodex.git
    cd prodex

(Recommended) Set up a virtual environment:

    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies:
    
    pip install -r requirements.txt

## Usage
Execute the script:
    
    python prodex.py

## Testing
Run the tests
    
    py.test tests

## License
This project is published under the MIT License.