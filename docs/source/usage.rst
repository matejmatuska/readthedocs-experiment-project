Usage
=====

.. _installation:

Installation
------------

To use framework, first install it using pip:

.. code-block:: console

   (.venv) $ pip install framework

Producing messages
------------------

To define a new type of message, extend the ``framework.Model`` class:

.. autoclass:: framework.Model

You can dump info about the Model with the :py:func:`framework.Model.dump` function:

.. autofunction:: framework.Model.dump

For example:

>>> import framework
>>> class MyModel(framework.Model):
>>>     self.name = 'whatever'
>>>
>>> model = MyModel()
>>> model.dump()

