from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
import logging
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from gergelypolonkaiweb.solarized_dark import SolarizedDarkStyle

register = template.Library()

class CodeFormatter(HtmlFormatter):
    def wrap(self, source, outfile):
        return self._wrap_code(source)

    def _wrap_code(self, source):
        yield 0, "<pre class=\"" + self.cssclass + "\"><ol>"
        for i, t in source:
            if i == 1:
                t = "<li>" + t + "</li>"

            yield i, t
        yield 0, "</ol></pre>"

@register.filter(needs_autoescape=True)
@stringfilter
def syhilite(value, language, autoescape=None):
    if language == "php":
        value = "<?php\n" + value

    lexer = get_lexer_by_name(language)
    formatter = CodeFormatter(style = SolarizedDarkStyle, linenos = False, cssclass = language + " code", noclasses = True)
    html = highlight(value, lexer, formatter)
    css = formatter.get_style_defs(['.code-chunk .code'])
    return mark_safe(html)

