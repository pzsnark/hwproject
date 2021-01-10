from django.forms.widgets import Widget
from django.template import loader
from django.utils.safestring import mark_safe


class AudioWidget(Widget):
    template_name = 'ads/audio_widget.html'

    def get_context(self, path, value, attrs=None):
        return {'widget': {
            'path': path,
        }}

    def render(self, path, attrs=None):
        context = self.get_context(path, attrs)
        template = loader.get_template(self.template_name).render(context)
        return mark_safe(template)
