class AnonymousSurvey:
    """Collect anonymous answer to a survey question."""
    def __init__(self,question) -> None:
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self) -> None:
        """Show survey question."""
        print(self.question)
    
    def store_response(self,new_response) -> None:
        """Store singe response to a survey
        params
        new_response -> string : new response
        """
        self.responses.append(new_response)

    def show_results(self) -> None:
        """Show all the responses that have been given."""
        print("Survey results.")
        for response in self.responses:
            print(f" -> {response}")
