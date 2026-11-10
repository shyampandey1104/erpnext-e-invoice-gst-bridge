"""Unit tests for GSTInvoiceBridge."""

from gst_bridge.irn_generator import GSTInvoiceBridge, EInvoiceDocument, EInvoiceItem


def test_irn_hash_generation():
    irn = GSTInvoiceBridge.generate_irn_hash(
        supplier_gstin="27AABCA1234F1Z5",
        doc_num="SINV-001",
        fin_year="2026-2027",
        doc_type="INV",
    )
    assert len(irn) == 64  # SHA-256 standard hex length
    assert isinstance(irn, str)


def test_nic_payload_formatting():
    doc = EInvoiceDocument(
        supplier_gstin="27AABCA1234F1Z5",
        buyer_gstin="29XYZAB5678K1Z2",
        document_number="SINV-001",
        document_date="10/11/2026",
        total_invoice_value=11800.0,
        items=[
            EInvoiceItem(
                item_name="Industrial Lubricant",
                hsn_code="27101990",
                qty=10.0,
                unit_rate=1000.0,
                taxable_value=10000.0,
                gst_rate=18.0,
                cgst_amount=0.0,
                sgst_amount=0.0,
                igst_amount=1800.0,
                total_amount=11800.0,
            )
        ],
    )
    payload = GSTInvoiceBridge.format_nic_payload(doc)
    assert payload["Version"] == "1.1"
    assert payload["SellerDtls"]["Gstin"] == "27AABCA1234F1Z5"
    assert len(payload["ItemList"]) == 1
