import logging
from tinydb import TinyDB, Query

logging.basicConfig(level=logging.INFO)
def select(db, key, val):
    Dog = Query()
    result = db.search(Dog[key] == val)
    logging.info(f'Search results: {result}')

def insert(db, val):
    db.insert(val)

def main():
    db = TinyDB('db.json')
    dogs: list = [
        {"id": 1, "breed": "Lab", "color": "Black"},
        {"id": 2, "breed": "Poodle", "color": "White"},
        {"id": 3, "breed": "Mutt", "color": "Mix"},
        {"id": 4, "breed": "Shepard", "color": "Black"},
        {"id": 5, "breed": "Beagle", "color": "Mix"}   
    ]

    for dog in dogs:
        insert(db, dog)

    select(db, 'id', 1)

if __name__ == '__main__':
    main()