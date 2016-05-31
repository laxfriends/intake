from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse

from jinja2 import Environment
from datetime import datetime
from pytz import timezone
from jinja2 import Markup

def namify(s=''):
    words = s.split()
    if not words:
        return s
    first_word = words[0].capitalize()
    return ' '.join([first_word] + words[1:])

class Linkifier:
    def __init__(self, links):
        self.links = links

    def build_link(self, lookup):
        url = self.links[lookup]
        return '<a href="{}">{}</a>'.format(
            url, lookup)

    def __call__(self, content):
        output = content
        for str_lookup in self.links:
            if str_lookup in content:
                link = self.build_link(str_lookup)
                output = content.replace(str_lookup, link)
        return Markup(output)


def current_local_time(fmt):
    utc_now = timezone('GMT').localize(datetime.utcnow())
    return utc_now.astimezone(timezone('US/Pacific')).strftime(fmt)


def add_content_constants():
    from project import content_constants
    linkify_links = {
        "Code for America": "https://codeforamerica.org",
        # "Privacy Policy": reverse("public.privacy_policy"),
        "Clean Slate": "http://sfpublicdefender.org/services/clean-slate/",
        "clearmyrecord@codeforamerica.org": "mailto:clearmyrecord@codeforamerica.org",
        "(415) 301-6005": "tel:14153016005"
    }
    return dict(
        content=content_constants,
        linkify=Linkifier(linkify_links),
        current_local_time=current_local_time,
        namify=namify
        )

class JinjaConfig:

    def __init__(self):
        self.env = None

    def __call__(self, **options):
        env = Environment(**options)
        env.globals.update({
            'static': staticfiles_storage.url,
            'url': reverse,
        })
        env.globals.update(add_content_constants())
        self.env = env
        return env

jinja_config = JinjaConfig()
    
