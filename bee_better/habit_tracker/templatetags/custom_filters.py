from typing import Union

from django import template

register = template.Library()


@register.filter()
def cell_conditional_formatting(variable: Union[bool, None]):
    """
    Update background color of the cell depends on value.
    """
    if variable:
        return "background-color: #bde9ba;"  # if cell has value of "True"
    else:
        if variable == "":
            return ""  # if cell has no value
        return "background-color: #f57c67;"  # if cell has value of "False"
