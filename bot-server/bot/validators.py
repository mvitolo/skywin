from os.path import splitext
import re

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions


def is_true(value):
    if value is False:
        raise ValidationError(u'You need to check this field to proceed')


def is_pdf_file_extension(value):
    ext = splitext(value.name)[1]
    valid_extensions = ['.pdf']
    if ext not in valid_extensions:
        raise ValidationError(u'This file type is not supported.')


def is_alphanumeric_file_name(value):
    file_name = splitext(value.name)[0]
    pattern = '^[a-zA-Z0-9-_/ ]+$'
    match = re.search(pattern, file_name)
    if not match:
        raise ValidationError(u'Please, make sure that the filename is composed only of alphanumeric characters.')


def is_below_max_size(value):
    try:
        if value.file.size > settings.FILE_UPLOAD_MAX_MEMORY_SIZE:
            raise ValidationError(u"Image file too large (maximum admitted is %dMB)" % (
                settings.FILE_UPLOAD_MAX_MEMORY_SIZE / (1024 * 1024)))
    except:
        pass


def is_image_ratio_compliant(value):
    width, height = get_image_dimensions(value.file)
    if not (0.5 < width/float(height) < 0.8):
        raise ValidationError(
            u"Image dimension is not valid (height=%ipx, width=%ipx); a valid ratio should be"
            u" about 2:3" % (width, height))


def is_file_name_length_compliant(value):
    file_name = splitext(value.name)[0]
    if len(file_name) > settings.IMG_NAME_MAX_LEN:
        raise ValidationError(u"Image name should be shorter than %d chars" % settings.IMG_NAME_MAX_LEN)
