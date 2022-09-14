from tkinter.ttk import Widget
from dbutils_typehint.fs import FS
from dbutils_typehint.secrets import Secrets
from dbutils_typehint.widgets import Widgets


class DBUtils:
    fs = FS()
    secrets = Secrets()
    widgets = Widgets()
