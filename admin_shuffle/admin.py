from django.conf import settings
from django.contrib import admin
from django.contrib.admin.views.main import ORDER_VAR, ChangeList as BaseChangeList
from django.contrib.admin.options import csrf_protect_m

SHUFFLE_QS_VALUE = getattr(settings, 'SHUFFLE_QS_VALUE', 'SHUFFLE')
SHUFFLE_LABEL = getattr(settings, 'SHUFFLE_LABEL', 'SHUFFLE')


class ChangeList(BaseChangeList):

    def get_ordering(self, request, queryset):
        if self.params.get(ORDER_VAR) == SHUFFLE_QS_VALUE:
            return ['?']
        return super(ChangeList, self).get_ordering(request, queryset)


class AdminShuffleMixin(object):
    admin_shuffle_change_list_template = 'admin_shuffle/change_list.html'

    def __init__(self, *args, **kwargs):
        super(AdminShuffleMixin, self).__init__(*args, **kwargs)
        if self.change_list_template:
            self.super_change_list_template = self.change_list_template
        else:
            self.super_change_list_template = 'admin/change_list.html'
        self.change_list_template = self.admin_shuffle_change_list_template

    def changelist_view(self, request, extra_context=None):
        request.GET._mutable = True
        request.GET[ORDER_VAR] = SHUFFLE_QS_VALUE
        request.GET._mutable = False

        qs = '?' + request.GET.urlencode()

        if not extra_context:
            extra_context = {}
        extra_context.update({
            'super_change_list_template': self.super_change_list_template,
            'shuffle_qs': qs,
            'shuffle_label': SHUFFLE_LABEL,
        })
        return super(AdminShuffleMixin, self).changelist_view(request, extra_context=extra_context)

    def get_changelist(self, request, **kwargs):
        return ChangeList
