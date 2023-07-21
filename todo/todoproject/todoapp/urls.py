from django.urls import path

from. import views
urlpatterns=[
    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name="update"),
    #path('details/',views.details,name="details")
    path('cbhome/',views.Tasklistview.as_view(),name="cbhome"),
    path('cbdetails/<int:pk>/',views.Taskdetailview.as_view(),name="cbdetails"),
    path('cbupdate/<int:pk>/',views.Taskupdateview.as_view(),name="cbupdate"),
    path('cbdelete/<int:pk>/',views.Taskdeleteview.as_view(),name="cbdelete"),
]