from admin_shuffle.admin import ORDER_VAR, SHUFFLE_QS_VALUE
from django.contrib.admin.sites import AdminSite
from django.test import TestCase
from django.test import RequestFactory

from .admin import ArticleAdmin
from .models import Article


class MockSuperUser:
    is_active = True
    is_staff = True

    def has_perm(self, *args, **kwargs):
        return True


class AdminTests(TestCase):

    def setUp(self):
        self.site = AdminSite()
        self.admin = ArticleAdmin(Article, self.site)
        self.factory = RequestFactory()

    def test_shuffle(self):
        articles = []
        for x in range(100):
            articles.append(Article(
                title=x,
                content=100-x,
            ))
        Article.objects.bulk_create(articles)

        request = self.factory.get('/admin/tests/article/?{}={}'.format(
            ORDER_VAR, SHUFFLE_QS_VALUE
        ))
        request.user = MockSuperUser()
        cl = self.admin.get_changelist_instance(request)

        self.assertNotEqual(list(cl.root_queryset), list(cl.queryset))

    def test_template(self):
        request = self.factory.get('/admin/tests/article/')
        request.user = MockSuperUser()
        
        self.assertEqual(self.admin.original_change_list_template, 'tests/change_list.html')
        self.assertEqual(self.admin.change_list_template, 'admin_shuffle/change_list.html')
        self.assertIsNotNone(self.admin.changelist_view(request))

        ArticleAdmin.change_list_template = None
        admin = ArticleAdmin(Article, self.site)

        self.assertEqual(admin.change_list_template, 'admin_shuffle/change_list.html')
