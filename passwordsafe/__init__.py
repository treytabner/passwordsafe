VERSION = 0.1


def context_processor(request):
    return {
        'passwordsafe_version': VERSION,
    }
