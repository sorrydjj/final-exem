from django import template

register = template.Library()

@register.filter(name="an_status")
def an_status(user, status):
    print(user.announcement_user.filter(status=status).exclude(is_delete=True))
    return user.announcement_user.filter(status=status).exclude(is_delete=True)