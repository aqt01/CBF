from django import template


def get_element_name(element):
    return str(element._meta.verbose_name_plural)


def get_embed_url(url):
    youtube_video_code = url.split('=').pop()
    embed_url = "https://www.youtube.com/embed/" + youtube_video_code
    return embed_url


register = template.Library()
register.filter('get_element_name', get_element_name)
register.filter('get_embed_url', get_embed_url)
