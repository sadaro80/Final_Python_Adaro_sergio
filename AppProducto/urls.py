from django.urls import path
from . import views

urlpatterns=[
      path('', views.inicioproductos, name="inicioproductos"),
      path("productos/", views.lista_productos, name="lista_productos"),
      path("productos/<str:categoria>/", views.lista_productos, name="lista_productos_categoria"),
      path('alta_producto', views.producto_formulario, name='producto_formulario'),
      path('eliminar_producto/<int:id>', views.eliminar_producto, name='eliminar_producto'),
      path('editar_producto/<int:id>', views.editar_producto, name='editar_producto'),
      path('buscar_producto', views.buscar_producto, name='buscar_producto'),
      path('buscar', views.buscar, name='buscar'),
      path('login_admin/', views.login_admin_request, name='login_admin'),
      path('categoria/<str:categoria_nombre>/', views.productos_por_categoria, name='productos_por_categoria'),
      path('productos/<int:id>', views.vista_productos, name='vista_productos'),
      path('carrito/', views.vista_carrito, name='vista_carrito'),
      path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
      path('eliminar/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
      path('vaciar/', views.vaciar_carrito, name='vaciar_carrito'),
     



    ]