from contextlib import contextmanager
from database import Database
from database import Note

db = Database('banco')

# db.add(Note(title='Pão doce', content='Abra o pão e coloque o seu suco em pó favorito.'))
# db.add(Note(title=None, content='Lembrar de tomar água'))

# notes = db.get_all()
# for note in notes:
#     print(f'Anotação {note.id}:\n  Título: {note.title}\n  Conteúdo: {note.content}\n')

# update = notes[2]
# update.title = 'Pão salgado'
# update.content = 'Muito bom'
# db.update(update)

# db.delete(3)

# db.update(Note(id = 6, title='Água', content="Hidratem-se crianças!"))