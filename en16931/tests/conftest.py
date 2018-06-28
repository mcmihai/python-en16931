import pytest

from en16931.entity import Entity
from en16931.invoice import Invoice
from en16931.invoice_line import InvoiceLine
from en16931.tax import Tax


@pytest.fixture()
def invoice1():
    invoice = Invoice()
    seller = Entity(name="Acme Inc.", tax_scheme="VAT",
                    tax_scheme_id="ES34626691F", country="ES",
                    party_legal_entity_id="ES34626691F",
                    registration_name="Acme INc.", mail="acme@acme.io")
    buyer = Entity(name="Acme Inc.", tax_scheme="VAT",
                   tax_scheme_id="ES34626691F", country="ES",
                   party_legal_entity_id="ES34626691F",
                   registration_name="Acme INc.", mail="acme@acme.io")
    invoice.buyer_party = buyer
    invoice.seller_party = seller
    invoice.due_date = "2018-09-11"
    invoice.issue_date = "2018-06-11"
    # lines
    il1 = InvoiceLine(quantity=11, unit_code="EA", price=2,
                      item_name='test 1', currency="EUR",
                      tax_percent=0.21, tax_category="AA")
    il2 = InvoiceLine(quantity=2, unit_code="EA", price=25,
                      item_name='test 2', currency="EUR",
                      tax_percent=0.21, tax_category="AA")
    il3 = InvoiceLine(quantity=5, unit_code="EA", price=3,
                      item_name='test 3', currency="EUR",
                      tax_percent=0.1, tax_category="A")
    invoice.add_lines_from([il1, il2, il3])
    return invoice


@pytest.fixture()
def tax1():
    return Tax(0.21, "AA", None)


@pytest.fixture()
def tax2():
    return Tax(0.1, "A", None)
