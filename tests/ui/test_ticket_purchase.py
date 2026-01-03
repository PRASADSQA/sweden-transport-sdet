from pages.ticket_page import TicketPage

def test_ticket_purchase(page):
    page.goto("https://demo-ticketing.se/dashboard")
    ticket = TicketPage(page)
    ticket.buy_ticket()
    assert ticket.is_confirmed()