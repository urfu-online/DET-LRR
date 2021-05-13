# -*- coding: utf-8 -*-
import logging

from django.core.paginator import Paginator
from django.views.generic import ListView

logger = logging.getLogger(__name__)

class FilteredListView(ListView):
    allow_empty = True
    filterset_class = None
    filterset = None
    paginator_class = Paginator

    def get_paginator(self, queryset, per_page, orphans=0,
                      allow_empty_first_page=True, **kwargs):
        """Return an instance of the paginator for this view."""
        return self.paginator_class(
            queryset, per_page, orphans=orphans,
            allow_empty_first_page=self.allow_empty, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        qs = self.filterset.qs.distinct()
        if qs.count() == 0:
            self.paginate_by = None
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context
