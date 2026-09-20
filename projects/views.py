from django.shortcuts import render, get_object_or_404
from .models import Project



def project_list(request):

    status = request.GET.get('status')

    projects = Project.objects.all()

    if status in dict(Project.STATUS_CHOICES):
        projects = projects.filter(
            status=status
        )
    else:
        status = None

    featured_projects = Project.objects.filter(
        featured=True
    )[:6]

    context = {
        'projects': projects,
        'featured_projects': featured_projects,

        'total_projects': Project.objects.count(),

        'ongoing_count': Project.objects.filter(
            status='Ongoing'
        ).count(),

        'completed_count': Project.objects.filter(
            status='Completed'
        ).count(),

        'planning_count': Project.objects.filter(
            status='Planning'
        ).count(),

        'suspended_count': Project.objects.filter(
            status='Suspended'
        ).count(),

        'selected_status': status,
    }

    return render(
        request,
        'projects/project_list.html',
        context
    )

def project_detail(request, slug):

    project = get_object_or_404(
        Project,
        slug=slug
    )

    return render(
        request,
        'projects/project_detail.html',
        {
            'project': project
        }
    )

def featured_projects(request):

    projects = Project.objects.filter(
        featured=True
    )[:4]

    return render(
        request,
        'projects/featured_projects.html',
        {
            'projects': projects
        }
    )

