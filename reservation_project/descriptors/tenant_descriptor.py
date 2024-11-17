from validation.tenant_validation import validate_age


class TenantDescriptor:
    # Минимальный и максимальный возрасты для заключения договора
    MIN_AGE: int = 18
    MAX_AGE: int = 99

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.name == "_age":
            validate_age(value, TenantDescriptor.MIN_AGE, TenantDescriptor.MAX_AGE)
        instance.__dict__[self.name] = value
