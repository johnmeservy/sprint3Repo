from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from django.core.mail import send_mail

templater = get_renderer('homepage')

##########################################################################
# shows the list of orders


@view_function
def process_request(request):
    send_mail('Receipt', 'Thank you for ordering from The Colonial Heritage Foundation!', 'from@example.com', ['meservy@gmail.com'], fail_silently=False)
    return templater.render_to_response(request, 'receipt.html')
