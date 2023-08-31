Producing messages
------------------

To define a new type of message, extend the ``framework.Model`` class:

.. autoclass:: framework.Model
   :no-index:

You can dump info about the Model with the :py:func:`framework.Model.dump` function:

.. autofunction:: framework.Model.dump
   :no-index:

For example:

>>> import framework
>>> class MyModel(framework.Model):
>>>     self.name = 'whatever'
>>>
>>> model = MyModel()
>>> model.dump()
