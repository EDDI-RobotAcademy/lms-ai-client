class GeneratedRecipeResponse:
    def __init__(self, protocolNumber, recipe):
        self.protocolNumber = protocolNumber
        self.recipe = recipe

    def __str__(self):
        return f"GeneratedRecipeResponse(protocolNumber={self.protocolNumber}, \n\nrecipe>>>>\n{self.recipe}\n"
