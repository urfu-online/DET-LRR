from django.core.paginator import Paginator
from django.views.generic import ListView
from django_filters.views import FilterView


class FilteredListView(ListView, FilterView):
    allow_empty = True
    filterset_class = None
    filterset = None
    paginator_class = Paginator
    formhelper_class = None

    def get_filterset(self, filterset_class):
        kwargs = self.get_filterset_kwargs(filterset_class)
        filterset = filterset_class(**kwargs)
        filterset.form.helper = self.formhelper_class()
        return filterset

    def get_paginator(self, queryset, per_page, orphans=3,
                      allow_empty_first_page=True, **kwargs):
        """Return an instance of the paginator for this view."""
        return self.paginator_class(
            queryset, per_page, orphans=orphans,
            allow_empty_first_page=self.allow_empty, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        qs = self.filterset.qs  # .distinct()
        if not qs.exists():
            self.paginate_by = None
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context
