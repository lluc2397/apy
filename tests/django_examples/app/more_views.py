from django.views.generic import View


class APISubTestView(View):
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class APISub2TestView(View):
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class APISub3TestView(View):
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)
