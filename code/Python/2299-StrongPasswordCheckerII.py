class Solution(object):
    def strongPasswordCheckerII(self, password):
        """
        :type password: str
        :rtype: bool
        """
        if len(password) < 8:
            return False
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = "0123456789"
        special = "!@#$%^&*()-+"
        has_lower = False
        has_upper = False
        has_digit = False
        has_special = False
        two_same_adjacent = False
        for i in password:
            if i in lowercase:
                has_lower = True
                break
        for i in password:
            if i in uppercase:
                has_upper = True
                break
        for i in password:
            if i in digits:
                has_digit = True
                break
        for i in password:
            if i in special:
                has_special = True
                break
        for i in xrange(len(password)-1):
            if password[i] == password[i+1]:
                two_same_adjacent = True
                break
        return has_lower and has_upper and has_digit and has_special and not two_same_adjacent
                