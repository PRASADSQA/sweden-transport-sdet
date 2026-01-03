class TicketPage:
    def __init__(self, page):
        self.page = page
        self.buy_button = "#buyTicket"
        self.confirmation = "#confirmation"

    def buy_ticket(self):
        self.page.click(self.buy_button)

    def is_confirmed(self):
        return self.page.is_visible(self.confirmation)