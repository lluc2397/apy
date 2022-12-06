from django.views.generic import View


class APITestView(View):
    """A test view that will return the instance of a model

    Parameters
    ----------
        slug: str
            The slug of the model to retrieve
        id: int
            The id or pk of the model
    
    Returns
    -------
        model: object
            An instance of the model
    """
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

