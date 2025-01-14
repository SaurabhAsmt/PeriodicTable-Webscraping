import sqlite3
from itemadapter import ItemAdapter
import copy
import json
import logging

class GroupedElmsPipeline:
    def __init__(self):
        self.elems = {}

    def process_item(self, item, spider):
        logging.debug(f"Processing item: {item}")
        if item is None:
            raise ValueError("Received a None item")
        cg = item['chemical_group']

        if cg not in self.elems:
            self.elems[cg] = {"element_count": 0, "elements": []}

        item_copy = copy.deepcopy(item) # creates a copy of item
        del item_copy['chemical_group'] # deleting chemical group because we are adding this
                                        # self.elems[cg] = {"element_count": 0, "elements": []} again
        self.elems[cg]['elements'].append(dict(item_copy))
        self.elems[cg]['element_count'] += 1

        return item

    def close_spider(self, spider):
        with open("grouped_elms.json", "w") as file:
            json.dump(self.elems, file)



class PeriodicTbPipeline:
    def __init__(self):
        self.conn = sqlite3.connect("periodic_elms.db")
        self.cursor = self.conn.cursor()

    def open_spider(self, spider):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS periodic_elements (
        symbol TEXT PRIMARY KEY,
        name TEXT,
        atomic_number INTEGER,
        atomic_mass REAL,
        chemical_group TEXT
        )
        """)
        self.conn.commit()


    def process_item(self, item, spider):
        self.cursor.execute("INSERT OR IGNORE INTO periodic_elements VALUES (?,?,?,?,?)",(
                            item["symbol"],
                            item["name"],
                            item["atomic_number"],
                            item["atomic_mass"],
                            item["chemical_group"]
                            ))
        self.conn.commit()
        return item
    def close_spider(self, spider):
        self.conn.close()

