
from django.urls import path
from .import views as v

urlpatterns = [
    path('', v.home),
    path('addemp', v.add_emp),
    path('listemp', v.list_emp),
    path('deleteemp/<int:id>', v.delete_emp),
    path('editemp/<int:id>', v.edit_emp),
    path('deleteemp2', v.delete_emp2),
    path('addacc', v.add_acc),
    path('listacc', v.list_acc),
    path('deleteacc/<int:id>', v.delete_acc),
    path('editacc/<int:id>', v.edit_acc),
    path('addedu', v.add_edu),
    path('listedu', v.list_edu),
    path('deleteedu/<int:id>', v.delete_edu),
    path('editedu/<int:id>', v.edit_edu),
    path('addedu2', v.add_edu2),
    path('listedu2', v.list_edu2),
    path('deleteedu2/<int:id>', v.delete_edu2),
    path('editedu2/<int:id>', v.edit_edu2),
    path('addpro', v.add_pro),
    path('listpro', v.list_pro),
    path('editpro/<int:id>', v.edit_pro),
    path('deletepro/<int:id>', v.delete_pro),

]
