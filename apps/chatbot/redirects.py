 
from apps.base.BaseRedirect import *


class ChatRedirect(BaseRedirect):
    """كلاس موسع مع محادثة قبل إعادة التوجيه"""


    def __init__(self):
        super().__init__()

    def redirect(self, data, url=None, redirect_type: RedirectType = None, user_input=None):
        """إعادة تعريف دالة التوجيه مع إضافة المحادثة قبل التوجيه"""
        # المحادثة مع المستخدم
        if user_input:
            print(f"محادثة: {user_input}")
            response = f"تم تلقي المدخلات: {user_input}. هل ترغب في متابعة التوجيه؟"
            print(response)
        
        # تنفيذ التوجيه بعد المحادثة
        return super().redirect(data, url, redirect_type)