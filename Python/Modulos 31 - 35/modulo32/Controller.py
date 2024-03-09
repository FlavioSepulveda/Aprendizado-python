class Controller:
    def __init__(self, model, view):
        self.model=model
        self.view=view
        
    def save(self, email):
        try:
            self.model.email = email
            self.model.save()
            self.view.show_success(f'The email {email} is saved.')
        except ValueError as error:
            self.view.show_error(error)
            
        