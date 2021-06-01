import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
from Show import ShowGenre, ShowType

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "browser.ui")


class BrowserApp:
    def __init__(self, parent):
        self.start_ui(parent)
        self.setup_genre_combo()
        self.setup_type_combo()

    def start_ui(self,parent):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('top_level', parent)
        builder.connect_callbacks(self)

        self.builder = builder
        self.genre_combo = builder.get_object('genre_combo', parent)
        self.type_combo = builder.get_object('type_combo', parent)
        self.min_votes_entry = builder.get_object('type_combo', parent)

    def setup_genre_combo(self):
        genres = ShowGenre.fetch_genres()
        self.genre_combo['values'] = [ShowGenre.ALL_GENRES] + [genre.get_genre() for genre in genres]
        self.genre_combo.current(0)

    def setup_type_combo(self):
        types = ShowType.fetch_types()
        self.type_combo['values'] = [ShowType.ALL_TYPES] + [type.get_type() for type in types]
        self.type_combo.current(0)

    def show_imdb(self):
        pass

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Julian's ProjectS")
    app = BrowserApp(root)
    app.run()

