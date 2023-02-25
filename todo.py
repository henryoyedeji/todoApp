FILEPATH = "files/todos.txt"


class TodoApp:

    def __init__(self):
        self._todo_list = None
        with open(FILEPATH, mode='r') as file:
            todo_list = file.readlines()
            self._todo_list = {str(todo_list.index(todo) + 1): todo.strip('\n') for todo in todo_list}

    @property
    def todo(self):
        if self._todo_list:
            return self._todo_list
        else:
            return "You do not have any item in your todo list yet"

    @todo.setter
    def todo(self, item, todo_id=None):
        try:
            if todo_id:
                self._todo_list[todo_id] = item
            elif self._todo_list is None:
                self._todo_list[1] = item
            else:
                self._todo_list[len(self._todo_list) + 1] = item
        except KeyError:
            return "Something went wrong"

    def delete_todo(self, key):
        try:
            del self._todo_list[str(key)]
        except KeyError:
            return "Something went wrong"

    def write_to_file(self):
        with open(FILEPATH, mode='w') as file:
            for item in self._todo_list.values():
                file.write(item + '\n')
