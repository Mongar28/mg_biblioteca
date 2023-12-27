from trytond.model import ModelSQL, ModelView, fields


class User(ModelSQL, ModelView):
    'Usuarios'
    __name__ = 'mg.user'
    name = fields.Char("Name")
    status = fields.Selection([('active', "Active"),
                               ('inactive', "Inactive"),
                               ('defaulter', "Defaulter")], "Status")
    cedula = fields.Char("Cedula")

    @classmethod
    def default_status(cls):
        return "active"
