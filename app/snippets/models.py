from django.db import models

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


# Create your models here.
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True)
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    # linenos를 하면 줄 번호가 삽입된다.
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=True)
    highlighted = models.TextField()

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kargs):
        '''
        `pygments` 라이브러리를 사용해서, 하이라이트된 코드를 만든다.
        '''

        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'title' or False
        options = self.title and {'title': self.title} or {}
        formmater = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formmater)
        super(Snippet, self).save(*args, **kargs)
