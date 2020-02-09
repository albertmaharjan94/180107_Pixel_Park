from django import template
from ..models.Post import Post

register = template.Library()


@register.filter()
def has_like(value, uid):
    status=False
    if value.like_set.filter(user_id=uid):
        status=True
    return status
