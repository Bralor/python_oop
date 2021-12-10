import uuid
import random
import datetime


class TicketGenerator:
    """Create tickets from the given parameters."""
    fmt: str = "%d/%m/%y, %H:%M:%S"

    def __init__(self, user: str, issue: str):
        self.user = user
        self.issue = issue
        self.uuid: uuid.UUID = uuid.uuid4()
        self.date: str = datetime.datetime.now().strftime(self.fmt)


class CustomerSupport:
    """Process the tickets"""

    def __init__(self, priority: range):
        self.priority = priority
        self.tickets: list = []

    def create_ticket(self, user: str, issue: str) -> None:
        self.tickets.append(TicketGenerator(user, issue))

    def process_tickets(self) -> None:
        if not self.tickets:
            print("There are no unresolved tickets, well done..")
        else:
            for ticket in self.tickets:
                importance: int = random.choice(self.priority) # add specific value as parameter
                self.show_status(ticket, importance)

    def show_status(self, ticket: TicketGenerator, priority: int) -> None:
        print(
            f"Created: {ticket.date}",
            f"Processing ticket id: {ticket.uuid}",
            f"Issue: {ticket.issue}",
            f"Customer: {ticket.user}",
            f"Importance: {priority}",
            "=" * 58,
            sep="\n"
        )


if __name__ == "__main__":
    # vytvoření aplikace
    app = CustomerSupport(range(11))

    # registrace několika ticketů
    app.create_ticket("Petr Svetr", "Klimatizace v kanceláři A123 je rozbitá!")
    app.create_ticket("Matouš Nepříjemný", "Na záchodě je pouze dvouvrstvý toaletní papír.")
    app.create_ticket("Tereza Netrpělivá", "Indexování v PyCharmu trvá hrozně dlouho")

    # zpracování ticketů
    app.process_tickets()

