from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback-success')
    else:
        form = FeedbackForm()
    return render(request, 'formapp/feedback_form.html', {'form': form})

def feedback_success(request):
    return render(request, 'formapp/feedback_success.html')
