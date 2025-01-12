from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

@method_decorator(cache_page(60), name='dispatch')
class MessageListView(ListView):
    model = Message
    template_name = 'messages/list.html'
