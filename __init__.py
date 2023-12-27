from trytond.pool import Pool
from . import biblioteca, receptionist, user

__all__ = ['register']


def register():
    Pool.register(
        biblioteca.Biblioteca,
        receptionist.Receptionist,
        user.User,
        module='biblioteca', type_='model')
    Pool.register(
        module='biblioteca', type_='wizard')
    Pool.register(
        module='biblioteca', type_='report')
