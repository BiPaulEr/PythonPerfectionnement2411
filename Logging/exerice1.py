import logging
import random

livres_logger = logging.getLogger('livres')
transactions_logger = logging.getLogger('transactions')

livres_logger.setLevel(logging.WARNING)
transactions_logger.setLevel(logging.WARNING)

stream_handler = logging.StreamHandler()
livres_logger.addHandler(stream_handler)
transactions_logger.addHandler(stream_handler)

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