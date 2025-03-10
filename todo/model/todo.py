
from typing import List, Dict

class Todo:
    def __init__(self, title: str, description: str) -> None:
        # """Inicializa un nuevo objeto Todo con los parámetros title y description."""
        self.code_id: int = 0
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: List[str] = []

    def mark_completed(self) -> None:
        # """Marca el Todo como completado."""
        self.completed = True

    def add_tag(self, tag: str) -> None:
        # """Agrega un tag al Todo si no está presente ya."""
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self) -> str:
        # """Devuelve una representación en cadena del Todo."""
        return f"{self.code_id} - {self.title}"

class TodoBook:
    def __init__(self) -> None:
        # """Inicializa un nuevo TodoBook con un diccionario vacío."""
        self.todos: Dict[int, Todo] = {}

    def add_todo(self, title: str, description: str) -> int:
        # """Agrega un nuevo Todo al TodoBook y devuelve su ID."""
        new_id = len(self.todos) + 1
        todo = Todo(title, description)
        todo.code_id = new_id
        self.todos[new_id] = todo
        return new_id

    def pending_todos(self) -> List[Todo]:
        # """Devuelve una lista de todos los Todos pendientes (no completados)."""
        return [todo for todo in self.todos.values() if not todo.completed]

    def completed_todos(self) -> List[Todo]:
        # """Devuelve una lista de todos los Todos completados."""
        return [todo for todo in self.todos.values() if todo.completed]

    def tags_todo_count(self) -> Dict[str, int]:
        # """Devuelve un diccionario con la cantidad de cada tag en los Todos."""
        tag_count: Dict[str, int] = {}
        for todo in self.todos.values():
            for tag in todo.tags:
                if tag not in tag_count:
                    tag_count[tag] = 1
                else:
                    tag_count[tag] += 1
        return tag_count

