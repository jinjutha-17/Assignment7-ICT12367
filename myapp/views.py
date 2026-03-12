from django.shortcuts import render

def form_view(request):
    success = False

    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        if fullname and email and phone:
            success = True

    return render(request, 'form.html', {'success': success})
