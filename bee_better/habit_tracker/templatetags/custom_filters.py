from typing import Union

from django import template

register = template.Library()


@register.filter()
def cell_conditional_formatting(variable: Union[bool, None]):
    if variable:
        return "table-success"  # True
    else:
        if variable == "":
            return "table-warning"  # None
        return "table-danger"  # False
