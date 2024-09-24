# mainapp/management/commands/list_urls.py

from django.core.management.base import BaseCommand
from django.urls import get_resolver, URLPattern, URLResolver
from django.conf import settings
from django.urls import URLPattern, URLResolver

urlconf = __import__(settings.ROOT_URLCONF, {}, {}, [''])

class Command(BaseCommand):
    help = 'List all registered URLs'

    def handle(self, *args, **kwargs):
        self.stdout.write("Registered URL Patterns:")
        url_patterns = get_resolver().url_patterns
        self.list_urls(url_patterns)

    def list_urls(self, url_patterns, prefix=''):
        for p in self.inner_list_urls(urlconf.urlpatterns):
            print(''.join(p))
    def inner_list_urls(self,lis, acc=None):
        if acc is None:
            acc = []
        if not lis:
            return
        l = lis[0]
        if isinstance(l, URLPattern):
            yield acc + [str(l.pattern)]
        elif isinstance(l, URLResolver):
            yield from self.inner_list_urls(l.url_patterns, acc + [str(l.pattern)])
        yield from self.inner_list_urls(lis[1:], acc)

