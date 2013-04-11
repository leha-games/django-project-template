# -*- coding: utf-8 -*-
import uuid, os
from random import sample


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(instance.directory_string_var, filename)


def get_random(queryset, number, from_amount=False):
    ids = queryset.values_list('id', flat=True)
    if from_amount:
        ids = ids[:from_amount]
    amount = min(len(ids), number)
    picked_ids = sample(ids, amount)
    return queryset.filter(id__in=picked_ids)

