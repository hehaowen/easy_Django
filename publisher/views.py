from django.shortcuts import render
from publisher.models import Publisher


# Create your views here.
def Publisher_def(request):
    Publisher_all = Publisher.objects.all()
    return render(request, 'index.html' , {'Pub': Publisher_all})


def detail(request, id):
    pub_detail = Publisher.objects.get(id=id)
    return render(request, 'publisher/detail.html', {'pub_detail': pub_detail})

def Publisher_pub(request):
    pub_pub = Publisher.objects.all()
    return render(request,'publisher/publishers.html',{'pub_pub':pub_pub})