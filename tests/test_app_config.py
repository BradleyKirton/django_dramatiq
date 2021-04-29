from django_dramatiq.apps import DjangoDramatiqConfig


def test_default_task_autodiscover_modules():
    assert DjangoDramatiqConfig.task_autodiscover_modules() == ["tasks"]


def test_extra_task_autodiscover_modules(settings):
    settings.DRAMATIQ_AUTODISCOVER_MODULES = ("services",)
    autodiscover_modules = DjangoDramatiqConfig.task_autodiscover_modules()
    assert len(autodiscover_modules) == 2
    assert "tasks" in autodiscover_modules
    assert "services" in autodiscover_modules
