from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from admins.forms import UserAdminRegistrationForm, UserAdminProfileFrom
from users.models import User
# Create your views here.


@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {
        'title': 'GeekShop - Панель Администратора',
    }
    return render(request, 'admins/index.html', context)


class UserListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Пользователи'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch()


class UserCreateView(CreateView):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegistrationForm
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Создание пользователей'
        return context
    
    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch()


class UserUpdateView(UpdateView):
    model = User
    form_class = UserAdminProfileFrom
    success_url = reverse_lazy('admins:admin_users')
    template_name = 'admins/admin-users-update-delete.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data()
        context['title'] = 'GeekShop - Обновление пользователя'
        return context
    
    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch()


class UserDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.safe_delete()
        return HttpResponseRedirect(success_url)


# @user_passes_test(lambda u: u.is_staff)
# def admin_users(request):
#     context = {
#         'title': 'GeekShop - Пользователи',
#         'users': User.objects.all(),
#     }
#     return render(request, 'admins/admin-users-read.html', context)


# @user_passes_test(lambda u: u.is_staff)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     else:
#         form = UserAdminRegistrationForm()
#     context = {
#         'title': 'GeekShop - Создание пользователей',
#         'form': form,
#     }
#     return render(request, 'admins/admin-users-create.html', context)


# @user_passes_test(lambda u: u.is_staff)
# def admin_users_update(request, id):
#     selected_user = User.objects.get(id=id)
#     if request.method == 'POST':
#         form = UserAdminProfileFrom(instance=selected_user, files=request.FILES, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     else:
#         form = UserAdminProfileFrom(instance=selected_user)
#     context = {
#         'title': 'GeekShop - Обновление пользователя',
#         'form': form,
#         'selected_user': selected_user,
#     }
#     return render(request, 'admins/admin-users-update-delete.html', context)


# def admin_users_delete(request, id):
#     user = User.objects.get(id=id)
#     user.safe_delete()
#     return HttpResponseRedirect(reverse('admins:admin_users'))
