from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from django.http import HttpResponse
from .models import Material

def material_view(request):
    subject_id = request.GET.get('subject_id')
    year = request.GET.get('year')
    type=request.GET.get('type')
    material = Material.objects.filter(subject_id=subject_id, year=year, material_type=type, aproved=True).first()
    if material:
        # Assuming the material is stored as a file field named 'material'
        file_path = material.material.path
        # Serve the file using FileResponse
        return FileResponse(open(file_path, 'rb'))
    else:
        # No material available, render a custom HTML page
        return render(request, 'no_material.html')
    
# views.py

from django.shortcuts import render, redirect
from .forms import MaterialForm
# views.py

from django.shortcuts import render, redirect
from .forms import MaterialForm
from .models import Material

def create_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        
        if form.is_valid():
            subject = form.cleaned_data['subject']
            year = form.cleaned_data['year']
            
            # Check if a material already exists for the same semester, subject, and year
            existing_material = Material.objects.filter(subject=subject, year=year).exists()
            if existing_material:
                # If material already exists, return an error message
                error_message = "Material already exists for the same  subject, and year."
                return render(request, 'create_material.html', {'form': form, 'error_message': error_message})

            form.save()
            # Redirect to a success page or any other page after successfully creating the material
            return redirect('home')
    else:
        form = MaterialForm()
    return render(request, 'create_material.html', {'form': form})

