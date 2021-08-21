from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
  def __init__(self, request=None):
    
    super().__init__(request)
  
  def get_login_redirect_url(self, request):
    
    return "https://atrp.atrpforum.repl.co/"
  
