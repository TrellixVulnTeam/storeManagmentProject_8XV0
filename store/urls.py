from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('store', views.store, name="store"),
	path('productDetail/<str:pk>/', views.productDetail, name="productDetail"),
	path('womens/', views.womens, name="womens"),
	path('mens/', views.mens, name="mens"),
	path('summer/', views.summer, name="summer"),
	path('winter/', views.winter, name="winter"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

]