from django import template; register = template.Library()

import re
from itertools import chain


@register.inclusion_tag("_comment.html")
def render_comment(request, uid, comment, friends, root_comment=False):
    return locals()


class CompressNode(template.Node):

    def __init__(self, kind, nodelist):
        self.kind = kind
        self.nodelist = nodelist

    def render(self, context):
        compressor_string = settings.COMPRESSOR[self.kind]
        compressor = getattr(__import__(compressor_string))
        compressor.output()

@register.tag
def compress(parser, token):
    nodelist = parser.parse('endcompress')
    parser.delete_first_token()
    kind = token.split_contents()[1]
    return CompressNode(kind, nodelist)

