from django.contrib import admin
from .models import Category, Manufacturer, Product, Cart, CartItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country')
    search_fields = ('name', 'country')
    list_filter = ('country',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'category', 'manufacturer')
    search_fields = ('name',)
    list_filter = ('category', 'manufacturer')
    list_editable = ('price', 'stock')


class CartItemInline(admin.TabularInline):
    """Позволяет редактировать элементы корзины прямо на странице корзины"""
    model = CartItem
    extra = 1
    readonly_fields = ('item_cost',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'total_cost')
    inlines = [CartItemInline]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'quantity', 'item_cost')
    list_filter = ('cart',)