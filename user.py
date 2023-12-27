from trytond.model import ModelSQL, ModelView, fields


class User(ModelSQL, ModelView):
    'Usuarios'
    __name__ = 'mg.user'
    biblioteca = fields.Many2One('mg.biblioteca', "Biblioteca")
    name = fields.Char("Name")
    status = fields.Selection([('active', "Active"),
                               ('inactive', "Inactive"),
                               ('defaulter', "Defaulter")], "Status")
    cedula = fields.Char("Cedula")
