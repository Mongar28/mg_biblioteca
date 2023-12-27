from trytond.model import ModelSQL, ModelView, fields


class Biblioteca(ModelSQL, ModelView):
    "Biblioteca"
    __name__ = 'mg.biblioteca'

    name = fields.Char('Biblioteca')
    receptionists = fields.One2Many(
        'mg.receptionist', 'biblioteca', "Receptionist")
