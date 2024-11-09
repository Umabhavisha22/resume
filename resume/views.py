from django.shortcuts import render

def home(request):
    # Dummy data for the resume
    context = {
        'name': 'Your Name',
        'title': 'Your Job Title',
        'summary': 'A brief summary about yourself...',
        'experience': [
            {'job_title': 'Job Title 1', 'company': 'Company 1', 'description': 'Job description 1'},
            {'job_title': 'Job Title 2', 'company': 'Company 2', 'description': 'Job description 2'},
        ],
        'education': [
            {'degree': 'Degree 1', 'institution': 'Institution 1', 'year': 'Year 1'},
            {'degree': 'Degree 2', 'institution': 'Institution 2', 'year': 'Year 2'},
        ],
        'skills': ['Skill 1', 'Skill 2', 'Skill 3'],
    }
    return render(request, 'resume/home.html', context)
