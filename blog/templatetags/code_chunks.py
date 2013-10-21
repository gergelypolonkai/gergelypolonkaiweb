from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
import logging, re
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from gergelypolonkaiweb.solarized_dark import SolarizedDarkStyle
from blog.models import CodeChunk

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

def hilite(language, code):
    lexer = get_lexer_by_name(language)
    formatter = CodeFormatter(style = SolarizedDarkStyle, linenos = False, cssclass = language + " code", noclasses = True)
    return highlight(code, lexer, formatter)

@register.filter(needs_autoescape=True)
@stringfilter
def remove_code_chunks(value, autoescape=None):
    p = re.compile('\[\$ code:(?P<lang>[^:]+):(?P<slug>[^ ]+) \$\]')
    i = p.finditer(value)
    diff = 0

    for match in i:
        end, start = match.span()
        oldlen = start - end
        start += diff
        end += diff
        newstr = ""
        newlen = len(newstr)
        value = value[:end] + newstr + value[start:]
        diff += newlen - oldlen

    p = re.compile('\[\$ code:(?P<lang>[^:]+):(?P<code>.+?) \$\]', re.DOTALL)
    i = p.finditer(value)
    diff = 0

    for match in i:
        end, start = match.span()
        oldlen = start - end
        start += diff
        end += diff
        newstr = ""
        newlen = len(newstr)
        value = value[:end] + newstr + value[start:]
        diff += newlen - oldlen

    return mark_safe(value)

@register.filter(needs_autoescape=True)
@stringfilter
def insert_code_chunks(value, autoescape=None):
    p = re.compile('\[\$ code:(?P<lang>[^:]+):(?P<slug>[^ ]+) \$\]')
    i = p.finditer(value)
    diff = 0

    for match in i:
        end, start = match.span()
        oldlen = start - end
        start += diff
        end += diff
        try:
            chunk = CodeChunk.objects.get(language = match.group('lang'), slug = match.group('slug'))
            # TODO: This is an ugly hack, as it includes template logic in code. BAD!
            newstr = "<div class=\"code-chunk\">" + hilite(match.group('lang'), chunk.content) + "</div>"
        except CodeChunk.DoesNotExist:
            newstr = ""

        newlen = len(newstr)
        value = value[:end] + newstr + value[start:]
        diff += newlen - oldlen

    p = re.compile('\[\$ code:(?P<lang>[^:]+):(?P<code>.+?) \$\]', re.DOTALL)
    i = p.finditer(value)
    diff = 0

    for match in i:
        end, start = match.span()
        oldlen = start - end
        start += diff
        end += diff

        # TODO: This is an ugly hack, as it includes template logic in code. BAD!
        newstr = "<div class=\"code-chunk\">" + hilite(match.group('lang'), match.group('code')) + "</div>"

        newlen = len(newstr)
        value = value[:end] + newstr + value[start:]
        diff += newlen - oldlen

    return mark_safe(value)

@register.filter(needs_autoescape=True)
@stringfilter
def syhilite(value, language, autoescape=None):
    if language == "php":
        value = "<?php\n" + value

    html = hilite(language, value)
    return mark_safe(html)

