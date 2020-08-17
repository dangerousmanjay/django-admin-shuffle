from django.conf import settings
from django.contrib import admin
from django.contrib.admin.views.main import ChangeList, ORDER_VAR
from django.contrib.admin.options import csrf_protect_m

SHUFFLE_QS_VALUE = getattr(settings, 'SHUFFLE_QS_VALUE', 'SHUFFLE')
SHUFFLE_LABEL = getattr(settings, 'SHUFFLE_LABEL', 'SHUFFLE')


class ShuffleChangeList(ChangeList):

    def get_ordering(self, request, queryset):
        if self.params.get(ORDER_VAR) == SHUFFLE_QS_VALUE:
            return ['?']
        return super(ShuffleChangeList, self).get_ordering(request, queryset)


class AdminShuffleMixin(object):
    shuffle_change_list_template = 'admin_shuffle/change_list.html'

    def __init__(self, *args, **kwargs):
        super(AdminShuffleMixin, self).__init__(*args, **kwargs)
        if self.change_list_template:
            self.original_change_list_template = self.change_list_template
        else:
            self.original_change_list_template = 'admin/change_list.html'
        self.change_list_template = self.shuffle_change_list_template

    @csrf_protect_m
    def changelist_view(self, request, extra_context=None):
        if not extra_context:
            extra_context = {}
        extra_context.update({
            'original_change_list_template': self.original_change_list_template,
            'shuffle_qs_value': SHUFFLE_QS_VALUE,
            'shuffle_label': SHUFFLE_LABEL,
            'order_var': ORDER_VAR,
        })
        return super(AdminShuffleMixin, self).changelist_view(request, extra_context=extra_context)

    def get_changelist(self, request, **kwargs):
        return ShuffleChangeList
