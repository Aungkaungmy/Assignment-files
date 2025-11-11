# ============================================
# User Story #17 – Search Previous Request
# ============================================

from datetime import datetime

# --------------------------------------------------
# BOUNDARY
# --------------------------------------------------
class SearchPrevRequestPage:
    def __init__(self):
        self.controller = SearchPrevRequestController()

    # UML: +submitSearch(requestStatus, filterCriteria, data): str
    def submitSearch(self, requestStatus, filterCriteria, data):
        result_text = self.controller.searchRequest(requestStatus, filterCriteria, data)
        print(result_text)
        return result_text

    def run(self):
        print("=== Search Previous Request (Assistance System) ===")
        print(f"(Logged in as: {self.controller.pin})")

        while True:
            print("\nMenu:")
            print("  1) Search my requests")
            print("  2) Exit")
            choice = input("Enter your choice (1/2): ").strip()

            if choice == "2":
                print("Goodbye!")
                break

            elif choice == "1":
                # Gather search parameters
                requestStatus = input("Status (PENDING/IN_PROGRESS/COMPLETED): ").strip().upper()
                filterCriteria = input("Filter criteria (title/category/date range): ").strip()
                title = input("Title contains: ").strip()
                category = input("Category (transport/medical/housing/finance): ").strip()
                from_date = input("From date (YYYY-MM-DD): ").strip()
                to_date = input("To date (YYYY-MM-DD): ").strip()

                # 'data' carries keyword filters and other metadata
                data = {
                    "pin": self.controller.pin,
                    "title": title,
                    "category": category,
                    "from_date": from_date,
                    "to_date": to_date,
                }

                # Call controller
                self.submitSearch(requestStatus, filterCriteria, data)

            else:
                print("Invalid choice. Try again (1 or 2).")


# --------------------------------------------------
# CONTROLLER
# --------------------------------------------------
class SearchPrevRequestController:
    def __init__(self):
        self.entity = Request()
        self.pin = "PIN-123"  # Simulate logged-in user

    # UML: +searchRequest(requestStatus, filterCriteria, data): str
    def searchRequest(self, requestStatus, filterCriteria, data):
        data["pin"] = self.pin  # enforce logged-in user context
        return self.entity.searchRequest(requestStatus, filterCriteria, data)


# --------------------------------------------------
# ENTITY
# --------------------------------------------------
class Request:
    def __init__(self):
        self._requests = None
        # UML Attributes:
        # -requestID: int
        # -requestTitle: str
        # -requestCategory: str
        # -requestDate: str
        # -requestStatus: str

    def _init(self):
        if self._requests is None:
            self._requests = [
                {"id": 2001, "pin": "PIN-123", "title": "Transport to doctor",
                 "category": "transport", "date": "2025-09-01",
                 "status": "COMPLETED", "is_deleted": False},

                {"id": 2002, "pin": "PIN-123", "title": "Need for wheelchair",
                 "category": "medical", "date": "2025-10-10",
                 "status": "IN_PROGRESS", "is_deleted": False},

                {"id": 2003, "pin": "PIN-123", "title": "Home repair assistance",
                 "category": "housing", "date": "2025-08-12",
                 "status": "PENDING", "is_deleted": False},

                {"id": 2004, "pin": "PIN-999", "title": "Financial aid request",
                 "category": "finance", "date": "2025-10-02",
                 "status": "COMPLETED", "is_deleted": False},
            ]

    # UML: +searchRequest(requestStatus, filterCriteria, data): str
    def searchRequest(self, requestStatus, filterCriteria, data):
        self._init()

        pin = (data.get("pin") or "").strip()
        title = (data.get("title") or "").strip().lower()
        category = (data.get("category") or "").strip().lower()
        from_date = (data.get("from_date") or "").strip()
        to_date = (data.get("to_date") or "").strip()

        results = []
        for r in self._requests:
            # Must belong to this user and not deleted
            if r["pin"] != pin or r["is_deleted"]:
                continue

            # Filter by status (always provided in requestStatus)
            if requestStatus and requestStatus != r["status"].upper():
                continue

            # Optional filters
            if title and title not in r["title"].lower():
                continue
            if category and category != r["category"].lower():
                continue
            if from_date and r["date"] < from_date:
                continue
            if to_date and r["date"] > to_date:
                continue

            results.append(r)

        # Return message string
        if not results:
            return "\n[Error] No matched results found."

        lines = [f"\n=== Search Results ({len(results)} found) ==="]
        for r in results:
            lines.append(
                f"- ID: {r['id']} | Date: {r['date']} | "
                f"Category: {r['category']} | Status: {r['status']} | Title: {r['title']}"
            )
        return "\n".join(lines)


# --------------------------------------------------
# Run Program
# --------------------------------------------------
if __name__ == "__main__":
    page = SearchPrevRequestPage()
    page.run()
