class Error(Exception):

    """
    Base class for all exceptions.

    This is the base class for all exceptions raised within the
    Gumnut-Assembler context.

    :param expression: A string containing the expression which caused
                       the exception to be raised.

    :param message: A string containing some more information what could
                      raise such an exception.
    """

    def __init__(self, expression, message):
        super().__init__()
        self.type = type(self).__name__
        self.expression = expression
        self.message = message

    def __repr__(self):
        return str("Error <{self.type}, {self.message}, {self.expression}>")

    def as_dict(self):
        return dict({"type": self.type, "expression": self.expression, "message": self.message})


class InstructionMemorySizeExceeded(Error):

    """
    Get's raised when trying to upload more data into the instruction
    memory than it can hold.
    """


class DataMemorySizeExceeded(Error):

    """
    Get's raised when trying to upload more data into the data memory
    than it can hold.
    """


class UnknownInstruction(Error):

    """
    Get's raised when an unknown instruction is encountered.
    """
