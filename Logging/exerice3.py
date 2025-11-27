import logging
import random

class SensitiveFilter(logging.Filter):
    def filter(self, record):
        msg = record.getMessage()
        record.msg = msg.replace('User', "****")
        return True

livres_logger = logging.getLogger('livres')
transactions_logger = logging.getLogger('transactions')

livres_logger.setLevel(logging.WARNING)
transactions_logger.setLevel(logging.WARNING)

livres_handler = logging.StreamHandler()
livres_formatter = logging.Formatter("%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s", datefmt="%d/%Y %I/%M %p")
livres_handler.setFormatter(livres_formatter)
livres_handler.addFilter(SensitiveFilter())
livres_logger.addHandler(livres_handler)

transactions_handler = logging.StreamHandler()
transactions_formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
transactions_handler.setFormatter(transactions_formatter)
transactions_handler.addFilter(SensitiveFilter())
transactions_logger.addHandler(transactions_handler)

bibliotheque = {}

def add_book(title):
    if random.random() < 0.9:
        bibliotheque[title] = True
        livres_logger.info(f"{title} added")
    else:
        livres_logger.warning(f"{title} NOT added")

def process_transaction(user_id, book_id):
    if bibliotheque.get(book_id):
        transactions_logger.info(f"{user_id} buy {book_id}")
        bibliotheque.pop(book_id)
    else:
        transactions_logger.warning(f"{user_id} CANT buy {book_id}")


livres_a_ajouter = ["Livre_"+str(i).zfill(3) for i in range(1, 21)]
utilisateurs = ["User_"+str(i).zfill(3) for i in range(1, 4)]

for livre in livres_a_ajouter:
    add_book(livre)

for index, livre in enumerate(livres_a_ajouter):
    utilisateur = utilisateurs[index % len(utilisateurs)]
    process_transaction(utilisateur, livre)