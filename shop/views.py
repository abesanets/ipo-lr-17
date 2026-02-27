from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Manufacturer


def index(request):
    """Главная страница"""
    categories = Category.objects.all()
    return render(request, 'shop/index.html', {
        'categories': categories,
    })


def about(request):
    """Страница об авторе"""
    return render(request, 'shop/about.html')


def shop_info(request):
    """Страница о магазине"""
    return render(request, 'shop/shop_info.html', {
        'categories_count': Category.objects.count(),
        'products_count': Product.objects.count(),
        'manufacturers_count': Manufacturer.objects.count(),
    })


def product_list(request):
    """Каталог товаров с фильтрацией, поиском и сортировкой"""
    products = Product.objects.select_related('category', 'manufacturer').all()

    # === Поиск ===
    search_query = request.GET.get('search', '')
    if search_query:
        products = products.filter(name__icontains=search_query)

    # === Фильтр по категории ===
    selected_category = request.GET.get('category', '')
    if selected_category:
        products = products.filter(category__id=selected_category)

    # === Фильтр по производителю ===
    selected_manufacturer = request.GET.get('manufacturer', '')
    if selected_manufacturer:
        products = products.filter(manufacturer__id=selected_manufacturer)

    # === Фильтр по цене ===
    price_min = request.GET.get('price_min', '')
    if price_min:
        products = products.filter(price__gte=price_min)

    price_max = request.GET.get('price_max', '')
    if price_max:
        products = products.filter(price__lte=price_max)

    # === Сортировка ===
    sort = request.GET.get('sort', 'name')
    valid_sorts = ['name', '-name', 'price', '-price', '-stock']
    if sort in valid_sorts:
        products = products.order_by(sort)

    context = {
        'products': products,
        'categories': Category.objects.all(),
        'manufacturers': Manufacturer.objects.all(),
        'search_query': search_query,
        'selected_category': selected_category,
        'selected_manufacturer': selected_manufacturer,
        'price_min': price_min,
        'price_max': price_max,
        'sort': sort,
    }
    return render(request, 'shop/product_list.html', context)


def product_detail(request, product_id):
    """Детальная страница товара"""
    product = get_object_or_404(
        Product.objects.select_related('category', 'manufacturer'),
        id=product_id
    )
    return render(request, 'shop/product_detail.html', {
        'product': product,
    })