===================
Biblioteca Scenario
===================

Imports::

    >>> from proteus import Model, Wizard
    >>> from trytond.tests.tools import activate_modules

Activate modules::

    >>> config = activate_modules('biblioteca')

Crear biblioteca::

    >>> Biblioteca = Model.get('mg.biblioteca')
    >>> biblioteca = Biblioteca()
    >>> biblioteca.name = "Diogenes"
    >>> receptionist_one = biblioteca.receptionists.new(name='Mongar',status='contrated', genre='other')
    
    >>> receptionist_one.status == 'contrated'
    True
    
    >>> receptionist_two = biblioteca.receptionists.new(name='Ayala',status='proof', genre='female')
    >>> biblioteca.save()

    >>> biblioteca.name
    'Diogenes'
    >>> biblioteca.receptionists
    [proteus.Model.get('mg.receptionist')(1), proteus.Model.get('mg.receptionist')(2)]

    >>> user_one = biblioteca.users.new(name='Mongar',status='active', cedula ='11111111')

