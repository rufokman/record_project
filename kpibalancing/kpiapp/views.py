from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import redirect, render,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from .tables import *
from .filters import *
from django_tables2 import SingleTableView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
import django_tables2 as tables
from django_tables2.export.views import ExportMixin
from .forms import *
from django.utils.decorators import method_decorator


class CardAddView(TemplateView):
    template_name = "add_card_new.html"

    def get_queryset(self):
        return Card.objects.filter(user=self.request.user, delete=1)

    def get(self, *args, **kwargs):
        # Create an instance of the formset
        formset = CardFormSet(queryset=self.get_queryset())
        return self.render_to_response({'card_formset': formset})

    def post(self, request, *args, **kwargs):
        formset = CardFormSet(request.POST)
        print(self.request.user)
        print(self.request.user.function)
        print(formset.is_valid())

        # instances = formset.save(commit=False)
        # formset.save()
        # Check if submitted forms are valid
        # if formset.is_valid():
        #     print("formset is valid")
        #     instances = formset.save(commit=False)
        #     for instance in instances:
        #         instance.user = self.request.user
        #         instance.function = self.request.user.function
        #         instance.save()

        return render(request, self.template_name, {'card_formset': formset})


@login_required()
def cards_update(request):
    CardFormset = modelformset_factory(Card, form=CardsForm)
    queryset = Card.objects.all().filter(user=request.user, delete=1)
    formset = CardFormset(request.POST or None, queryset=queryset)
    if formset.is_valid():
        print("formset is valid")
        instances = formset.save(commit=False)
        for instance in instances:
            instance.user = request.user
            instance.function = request.user.function
            print(instance.function)
            instance.save()
    context = {
        'formset': formset,
                }
    return render(request, 'form.html', context)


@login_required
def AddCardView(request):

    queryset = Card.objects.all().filter(user=request.user, delete=1)
    form = CardsForm(request.POST or None)
    if form.is_valid():
        print("form is valid")

        qform = form.save(commit=False)
        qform.user = request.user
        qform.function = request.user.function
        qform.save()
    context = {'form': form, 'table_list': queryset}
    return render(request, 'tab.html', context=context)


class CardUpdateView(UpdateView):
    model = Card
    form_class = CardsForm
    template_name = 'edit_kpi.html'
    success_url = "/kpibalancing/"


class CardDeleteView(TemplateView):
    template_name = "delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = get_object_or_404(Card, pk=self.kwargs['pk'])
        data.delete = 0
        data.save(update_fields=['delete'])
        return context




# def table_create_view(request):
#     if request.user.is_superuser:
#         data = Card.objects.all()
#         form = CardsForm(instance=data)
#         if request.method == "POST":
#             form = CardsForm(request.POST, instance=data)
#             if form.is_valid():
#                 form.save()
#         context = {
#             'form': form
#         }
#         return render(request, 'admin_pivot_tab.html', context)
#
#     else:
#         table_list = Card.objects.all()
#         return render(request, 'pivot_tab.html', {'table_list': table_list})


class FilteredPeopleListView(SingleTableMixin, FilterView):
    table_class = CardTable
    model = Card
    template_name = "admin_pivot_tab_new.html"
    filterset_class = CardFilter