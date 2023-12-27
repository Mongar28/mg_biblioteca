from trytond.model import ModelSQL, ModelView, fields


class Receptionist(ModelSQL, ModelView):
    "Receptionist"
    __name__ = 'mg.receptionist'
    biblioteca = fields.Many2One('mg.biblioteca', "Biblioteca")
    name = fields.Char("Name")
    status = fields.Selection([('uncontrated', "Uncontrated"),
                               ('contrated', "Contrated"),
                               ('proof', "Proof")], "Status")
    genre = fields.Selection([('female', "Female"),
                              ('man', "Man"),
                              ('other', "Other")], "genre")
