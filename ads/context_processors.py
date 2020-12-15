from .forms import CategoryChoice


def proc_category(request):
    """Выбор категории для base.html"""
    return {
        'category_form': CategoryChoice()
    }
