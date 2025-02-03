# Scraping Periodic Table Elements

A Python script that utilizes the **Scrapy** and **Scrapy-Playwright** frameworks to scrape periodic table elements' data. The script retrieves dynamically loaded information, including the symbol, name, atomic number, atomic mass, and chemical group of each element.

## Features

- Scrapes detailed information for each periodic table element:
  - Symbol
  - Name
  - Atomic Number
  - Atomic Mass
  - Chemical Group
- Handles dynamically loaded content using **Scrapy-Playwright**.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure Playwright is properly installed and its browsers are set up:
   ```bash
   playwright install
   ```

## Usage

Run the Scrapy spider to scrape the periodic table data:

```bash
scrapy crawl <spider-name>
```

Replace `<spider-name>` with the name of the spider defined in your project.

## Dependencies

All dependencies are listed in the `requirements.txt` file. Ensure you have them installed before running the project.

## License

This project is licensed under the **GNU General Public License**. See the LICENSE file for more details.

---

Feel free to contribute or report issues to improve the project!
