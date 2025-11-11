# ================================================
# User Story #39 – Platform Management: Generate Weekly Report (BCE)
# ================================================

# --- Boundary ---
class GenerateReportPage:
    def __init__(self):
        self.controller = GenerateReportController()

    def submitGenerateReport(self, dateOption: str = "weekly") -> str:
        if dateOption.strip().lower() != "weekly":
            return "error message"
        return self.controller.generateReport(dateOption)

    def run(self):
        print("\n=== Platform Management - Generate Weekly Report ===")
        while True:
            print("\n1) Generate Weekly Report")
            print("2) Exit")
            choice = input("Enter your choice (1/2): ").strip()
            if choice == "1":
                print(self.submitGenerateReport("weekly"))
            elif choice == "2":
                print("Goodbye.")
                break
            else:
                print("error message")

# --- Controller ---
class GenerateReportController:
    def __init__(self):
        self.category = Category()
        self.userProfile = UserProfile()
        self.request = Request()

    def generateReport(self, dateOption: str) -> str:
        cats = self.category.generateReport()
        users = self.userProfile.generateReport()
        req_summary = self.request.generateReport(dateOption)  # returns dict of lists
        pending = len(req_summary["Pending"])
        assigned = len(req_summary["Assigned"])
        completed = len(req_summary["Completed"])
        return (
            "Report (weekly)\n"
            f"Categories: {len(cats)}\n"
            f"UserProfiles: {len(users)}\n"
            f"Requests Pending: {pending}\n"
            f"Requests Assigned: {assigned}\n"
            f"Requests Completed: {completed}"
        )

# --- Entity: Category ---
class Category:
    def __init__(self):
        self.categories = [
            {"categoryID": 1, "categoryName": "Healthcare"},
            {"categoryID": 2, "categoryName": "Education"},
            {"categoryID": 3, "categoryName": "Transport"},
        ]

    def generateReport(self) -> list:
        return list(self.categories)

# --- Entity: UserProfile ---
class UserProfile:
    def __init__(self):
        self.users = [
            {"userProfileID": 1, "userProfileName": "Alice", "userRole": "CSR", "userProfileStatus": "Active"},
            {"userProfileID": 2, "userProfileName": "Bob", "userRole": "PIN", "userProfileStatus": "Active"},
            {"userProfileID": 3, "userProfileName": "Clara", "userRole": "CSR", "userProfileStatus": "Inactive"},
            {"userProfileID": 4, "userProfileName": "Daniel", "userRole": "Admin", "userProfileStatus": "Active"},
        ]

    def generateReport(self) -> list:
        return list(self.users)

# --- Entity: Request ---
class Request:
    def __init__(self):
        self.requests = [
            {"PIN": "P001", "requestID": 1, "requestTitle": "Food Delivery Support",
             "requestCategory": "Transport", "requestStatus": "Pending",
             "requestDescription": "Delivering food", "requestDate": "2025-11-03",
             "requestLocation": "Jurong East", "CSRRepInCharge": "CSR_Anna", "shortlisted": True},
            {"PIN": "P002", "requestID": 2, "requestTitle": "Medical Aid Program",
             "requestCategory": "Healthcare", "requestStatus": "Assigned",
             "requestDescription": "Volunteer doctors", "requestDate": "2025-11-04",
             "requestLocation": "Woodlands", "CSRRepInCharge": "CSR_Ben", "shortlisted": True},
            {"PIN": "P003", "requestID": 3, "requestTitle": "Tutoring Program",
             "requestCategory": "Education", "requestStatus": "Completed",
             "requestDescription": "Weekly tutoring", "requestDate": "2025-11-06",
             "requestLocation": "Tampines", "CSRRepInCharge": "CSR_Clara", "shortlisted": False},
            {"PIN": "P004", "requestID": 4, "requestTitle": "Wheelchair Donation",
             "requestCategory": "Healthcare", "requestStatus": "Completed",
             "requestDescription": "Delivered wheelchairs", "requestDate": "2025-11-08",
             "requestLocation": "Clementi", "CSRRepInCharge": "CSR_David", "shortlisted": True},
        ]

    def generateReport(self, dateOption: str = "weekly") -> dict:
        out = {"Pending": [], "Assigned": [], "Completed": []}
        for r in self.requests:
            if r["requestStatus"] in out:
                out[r["requestStatus"]].append(
                    {"requestDate": r["requestDate"], "requestStatus": r["requestStatus"]}
                )
        return out

# --- Run ---
if __name__ == "__main__":
    GenerateReportPage().run()
