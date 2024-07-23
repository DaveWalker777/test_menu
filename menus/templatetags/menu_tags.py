from django import template
from menus.models import Menu

register = template.Library()


@register.inclusion_tag('menus/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    try:
        # Получаем меню и предзагружаем связанные элементы и их детей
        menu = Menu.objects.prefetch_related('items__children').get(name=menu_name)
        active_url = context['request'].path  # Получаем текущий URL
        active_item = find_active_item(menu.items.all(), active_url)  # Находим активный пункт меню
        return {
            'menu': menu,
            'active_item': active_item,
            'request': context['request'],
        }
    except Menu.DoesNotExist:
        # Если меню не существует, возвращаем пустой словарь
        return {'menu': None}


def find_active_item(items, active_url):
    # Рекурсивно находим активный пункт меню на основе текущего URL
    for item in items:
        if active_url == item.get_url():
            return item
        if item.children.exists():
            active_item = find_active_item(item.children.all(), active_url)
            if active_item:
                return active_item
    return None
