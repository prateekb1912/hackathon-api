from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
import os

@deconstructible
class FileTypeValidator:
    def __init__(self, allowed_types):
        self.allowed_types = allowed_types

    def __call__(self, value):
        ext = os.path.splitext(value.name)[1]
        if not ext.lower() in self.allowed_types:
            raise ValidationError(f'File type {ext} is not supported. Allowed types are: {", ".join(self.allowed_types)}.')


def validate_submission_file_type(value):
    validator = FileTypeValidator(['.png', '.jpg', '.jpeg', '.pdf'])
    validator(value)
