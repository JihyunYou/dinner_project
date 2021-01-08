from django.shortcuts import render
from django.views import generic
# Create your views here.
from dinner.models import CardInfo, UserInfo, Chit
from .forms import ChitForm
from django.shortcuts import render, get_object_or_404, redirect

def index(request):
    """View function for home page of site."""
    chits = Chit.objects.all()
    chits_dev1 = Chit.objects.filter(card__card_name__contains="개발운영1실")
    chits_dev2 = Chit.objects.filter(card__card_name__contains="개발운영2실")
    chits_str = Chit.objects.filter(card__card_name__contains="전략실")

    num_cards = CardInfo.objects.all().count()
    num_chits = Chit.objects.all().count()

    if request.method == "POST":
        form = ChitForm(request.POST)
        if form.is_valid():
            new_chit = form.save()
            # new_chit.author = request.user
            # new_chit.published_at = timezone.now()
            new_chit.save()
            return redirect('/')
    else:
        form = ChitForm()

    context = {
        'chits': chits,
        'chits_dev1': chits_dev1,
        'chits_dev2': chits_dev2,
        'chits_str': chits_str,
        'form': form,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def delete_chit(request, id):
	chit = Chit.objects.get(id = id)
	chit.delete()
	return redirect('/')

class ChitListView(generic.ListView):
    model = Chit
    context_object_name = 'chit_list'
    paginate_by = 1