class Mobile:
    def __init__(self,mobile_to_add):
        self.mobile = mobile_to_add

class Mobile_store:
    def __init__(self):
        self.mobiles = []
    def add_mobile(self,mobile_to_add):
        if isinstance(mobile_to_add, Mobile):
            self.mobiles.append(mobile_to_add.mobile)
        else:
            raise TypeError("Please provide object only")

# Code that allows objects and string
# _mobile1 = Mobile("iphone 9")
# _mobile2 = Mobile("iphone 19")
# _samsung = "SAMSUNG GALAXY S24 ULTRA"
# _ivenus = Mobile_store()
# _ivenus.add_mobile(_mobile1.mobile)
# _ivenus.add_mobile(_mobile2.mobile)
# _ivenus.add_mobile(_samsung)

# Implement code that only objects can be appended to Mobile_store class and not the plain string
_mobile1 = Mobile("iphone 9")
_mobile2 = Mobile("iphone 19")
_samsung = "SAMSUNG GALAXY S24 ULTRA"
_ivenus = Mobile_store()
_ivenus.add_mobile(_mobile1)
_ivenus.add_mobile(_mobile2)
# Uncomment to raise error
# _ivenus.add_mobile(_samsung)
print(_ivenus.mobiles)