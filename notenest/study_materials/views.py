# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse, HttpResponse
from .forms import MaterialForm
from .models import Material
from authentication.models import User
from django.core.mail import EmailMessage
import mimetypes

def material_view(request):
    subject_id = request.GET.get('subject_id')
    year = request.GET.get('year')
    type = request.GET.get('type')
    material = Material.objects.filter(subject_id=subject_id, year=year, material_type=type, aproved=True).first()
    if material:
        # Assuming the material is stored as a file field named 'material'
        file_path = material.material.path
        # Serve the file using FileResponse
        return FileResponse(open(file_path, 'rb'))
    else:
        # No material available, render a custom HTML page
        return render(request, 'no_material.html')

def create_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        
        if form.is_valid():
            subject = form.cleaned_data['subject']
            year = form.cleaned_data['year']
            material = form.cleaned_data['material']
            
            # Check if a material already exists for the same semester, subject, and year
            existing_material = Material.objects.filter(subject=subject, year=year).exists()
            if existing_material:
                # If material already exists, return an error message
                error_message = "Material already exists for the same subject and year."
                return render(request, 'create_material.html', {'form': form, 'error_message': error_message})

            saved_material = form.save()

            # Fetch all admins
            admins = User.objects.filter(is_staff=True)

            # Sending email with attachment to all admins
            for admin in admins:
                email = EmailMessage(
                    'Material Created',
                    'A new material has been created for subject {} in year {} with ID {}.'.format(subject, year, saved_material.material_id),
                    'from@example.com',  # Change this to your sender email address
                    [admin.email],  # Send to the admin's email
                )
                # Attach the file to the email with the correct content type
                content_type, encoding = mimetypes.guess_type(material.name)
                email.attach(material.name, material.file.read(), content_type)
                email.send()

            # Redirect to a success page or any other page after successfully creating the material
            return redirect('home')
    else:
        form = MaterialForm()
    return render(request, 'create_material.html', {'form': form})