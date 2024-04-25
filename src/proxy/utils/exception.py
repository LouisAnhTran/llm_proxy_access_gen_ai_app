
class InvalidRequestBody(Exception):
    """Custom exception class."""
    
    def __init__(self, message="An error occurred."):
        self.message = message
        super().__init__(self.message)

class InvalidModelName(Exception):
    """Custom exception class."""
    
    def __init__(self, message="An error occurred."):
        self.message = message
        super().__init__(self.message)

class InvalidModeModelSelection(Exception):
    """Custom exception class."""
    
    def __init__(self, message="An error occurred."):
        self.message = message
        super().__init__(self.message)

class NotSeeListOfQuestionYet(Exception):
    """Custom exception class."""
    
    def __init__(self, message="An error occurred."):
        self.message = message
        super().__init__(self.message)

class ErrorSendingInferenceOpenAIModel(Exception):
    """Custom exception class."""
    
    def __init__(self, message="An error occurred."):
        self.message = message
        super().__init__(self.message)

class ErrorSendingInferenceMockModel(Exception):
    """Custom exception class."""
    
    def __init__(self, message="An error occurred."):
        self.message = message
        super().__init__(self.message)