# ============================================
# User Story #19 – PIN Logout After Service Completion

# ============================================

# --- Boundary ---
class LogoutPage:
    """
    <<Boundary>> LogoutPage
    +submitLogout(): str
    """

    def __init__(self):
        self.controller = LogOutPageController()

    def submitLogout(self):
        # Simulate confirmation
        confirm = input("Do you want to log out after completing your service? (y/n): ").strip().lower()
        if confirm == "y":
            result = self.controller.submitLogout()
            return result
        else:
            return "Logout cancelled."

    def run(self):
        print("\n=== PIN Logout After Service Completion ===")
        msg = self.submitLogout()
        print(msg)


# --- Controller ---
class LogOutPageController:
    """
    <<Controller>> LogOutPageController
    +submitLogout(): str
    """

    def __init__(self):
        self.entity = UserAccount()

    def submitLogout(self):
        # Call entity to perform logout
        return self.entity.submitLogout()


# --- Entity ---
class UserAccount:
    """
    <<Entity>> UserAccount
    +submitLogout(): str
    """

    def __init__(self):
        self.is_logged_in = True

    def submitLogout(self):
        # Always return success message (matches UML sequence diagram)
        if self.is_logged_in:
            self.is_logged_in = False
            return "Logout successful."
        return "No active session found."


# --- Run Program ---
if __name__ == "__main__":
    page = LogoutPage()
    page.run()
