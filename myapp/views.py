from django.shortcuts import render

def form_view(request):
    if request.method == "POST":
        return render(request, 'form.html', {'success': True})
    
    return render(request, 'form.html')