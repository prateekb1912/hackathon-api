def get_submission_file_path(instance, filename):
    return f'hackathons/{instance.hackathon.id}/submissions/{instance.id}/{filename}'
