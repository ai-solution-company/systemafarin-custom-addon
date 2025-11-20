import frappe

def test_invoice_validate(doc, method):
    # فقط برای اینکه اگر تو hooks خط validate بود، ارور نگیری
    frappe.msgprint(f"سلام از iran_core (validate) 👋<br>Invoice: {doc.name}")


def on_sales_invoice_submit(doc, method):
    """
    وقتی Sales Invoice submit شد:
    جمع grand_total همه فاکتورهای submit شده این customer
    توی فیلد test_iran_core_invoice روی Customer ذخیره میشه
    """
    if not doc.customer:
        return

    _update_customer_invoice_total(doc.customer)


def on_sales_invoice_cancel(doc, method):
    """
    وقتی فاکتور cancel شد هم جمع دوباره محاسبه بشه
    """
    if not doc.customer:
        return

    _update_customer_invoice_total(doc.customer)


def _update_customer_invoice_total(customer_name: str):
    total = frappe.db.sql("""
        SELECT COALESCE(SUM(grand_total), 0)
        FROM `tabSales Invoice`
        WHERE docstatus = 1
          AND customer = %s
    """, (customer_name,))[0][0]

    frappe.db.set_value("Customer", customer_name, "custom_test_iran_core_invoice", total)
