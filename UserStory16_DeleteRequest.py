# ============================================
# User Story #16

from datetime import datetime



# B: Boundary (User Interface)

class DeleteRequestPage:
    def __init__(self):
        self.controller = DeleteRequestController()

    # corresponds to +deleteConfirm()
    def deleteConfirm(self, requestID):
        confirm = input(f"Are you sure you want to delete Request #{requestID}? (y/n): ").strip().lower()
        return confirm == "y"

    # corresponds to +deleteRequest(): str
    def deleteRequest(self):
        rid_text = input("Enter Request ID to delete: ").strip()
        if not rid_text.isdigit():
            return "[Error] Please enter a valid number (e.g., 2001)."
        rid = int(rid_text)

        if not self.deleteConfirm(rid):
            return "Delete cancelled."

        message = self.controller.deleteRequest(rid)
        return message

    def run(self):
        print("=== Delete Request (Assistance System) ===")
        print(f"(Logged in as: {self.controller.pin})")

        while True:
            print("\nMenu:")
            print("  1) Delete a request")
            print("  2) Exit")
            cmd = input("Enter command (1/2): ").strip()

            if cmd == "2":
                print("Goodbye!")
                break
            elif cmd == "1":
                msg = self.deleteRequest()
                print(msg)
            else:
                print("[Error] Invalid command.")


# --------------------------------------------------
# C: Controller (Logic / Flow Control)
# --------------------------------------------------
class DeleteRequestController:
    def __init__(self):
        self.entity = Request()
        self.pin = "PIN-123"  # Simulate logged-in user

    # corresponds to +deleteRequest(requestID): str
    def deleteRequest(self, requestID):
        result = self.entity.deleteRequest(requestID, self.pin)
        return result


# --------------------------------------------------
# E: Entity (Data + Database)
# --------------------------------------------------
class Request:
    def __init__(self):
        self._requests = None  # DB placeholder
        self.requestID = None  # attribute shown in UML

    # DB initialization
    def _init(self):
        if self._requests is None:
            self._requests = [
                {"id": 2001, "pin": "PIN-123", "title": "Transport to doctor",
                 "status": "COMPLETED", "is_deleted": False},
                {"id": 2002, "pin": "PIN-123", "title": "Need for wheelchair",
                 "status": "IN_PROGRESS", "is_deleted": False},
                {"id": 2003, "pin": "PIN-123", "title": "Home repair assistance",
                 "status": "PENDING", "is_deleted": False},
            ]

    # corresponds to +deleteRequest(requestID): str
    def deleteRequest(self, requestID, pin):
        self._init()
        for r in self._requests:
            if r["id"] == requestID:
                if r["pin"] != pin:
                    return "You can only delete your own requests."
                if r["is_deleted"]:
                    return "This request has already been deleted."
                r["is_deleted"] = True
                return f"Request #{r['id']} ('{r['title']}') deleted successfully."
        return "Request not found."


# --------------------------------------------------
# Run Program
# --------------------------------------------------
if __name__ == "__main__":
    page = DeleteRequestPage()
    page.run()
