

from typing import Any


class Widgets:
    """
    Provides utilities for working with notebook widgets. You can create different types of widgets and get their bound value.
    Databricks documentation for more info: https://docs.databricks.com/notebooks/widgets.html
    """

    def combobox(self, name: str, defaultValue: str, choices: list[Any], label: str) -> None:
        """
        Creates a combobox input widget with a given name, default value and choices
        """
        pass

    def dropdown(self, name: str, defaultValue: str, choices: list[Any], label: str) -> None:
        """
        Creates a dropdown input widget a with given name, default value and choices
        """
        pass

    def get(self, name: str) -> str:
        """
        Retrieves current value of an input widget
        """
        pass

    def getArgument(self, name: str, optional: str) -> str:
        """
        (DEPRECATED) Equivalent to get
        """
        pass
    
    def multiselect(self, name: str, defaultValue: str, choices: list[Any], label: str) -> None:
        """
        Creates a multiselect input widget with a given name, default value and choices
        """
        pass

    def remove(self, name: str) -> None:
        """
        Removes an input widget from the notebook
        """
        pass

    def removeAll(self) -> None:
        """
        Removes all widgets in the notebook
        """
        pass

    def text(self, name: str, defaultValue: str, label: str) -> None:
        """
        Creates a text input widget with a given name and default value
        """
        pass
