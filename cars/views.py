from django.shortcuts import render
from django.views.generic import DetailView
from .models import Car, Comment
from .forms import CommentForm

# Create your views here.
class CarDetailsView(DetailView):
    model = Car
    template_name = 'cars/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        form = CommentForm()
        context['comments'] = comments
        context['form'] = form
        return context
    
    def post(self, request, *args, **kwargs):
        form = CommentForm(data=self.request.POST)
        car = self.get_object()
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)