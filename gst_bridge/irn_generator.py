"""Indian GST E-Invoice & IRN computation gateway for ERPNext."""

import hashlib
import json
from typing import Dict, Any, List
from pydantic import BaseModel


class EInvoiceItem(BaseModel):
    item_name: str
    hsn_code: str
    qty: float
    unit_rate: float
    taxable_value: float
    gst_rate: float  # e.g. 18.0
    cgst_amount: float
    sgst_amount: float
    igst_amount: float
    total_amount: float


class EInvoiceDocument(BaseModel):
    supplier_gstin: str
    buyer_gstin: str
    document_number: str
    document_date: str  # DD/MM/YYYY
    total_invoice_value: float
    items: List[EInvoiceItem]


class GSTInvoiceBridge:
    """Computes statutory IRN (Invoice Reference Number) and signs payload."""

    @staticmethod
    def generate_irn_hash(supplier_gstin: str, doc_num: str, fin_year: str, doc_type: str = "INV") -> str:
        """Standard NIC SHA-256 algorithm for generating unique IRN."""
        raw_string = f"{supplier_gstin.upper()}{fin_year}{doc_type.upper()}{doc_num.upper()}"
        return hashlib.sha256(raw_string.encode("utf-8")).hexdigest()

    @staticmethod
    def format_nic_payload(doc: EInvoiceDocument) -> Dict[str, Any]:
        return {
            "Version": "1.1",
            "TranDtls": {"TaxSch": "GST", "SupTyp": "B2B", "RegRev": "N"},
            "DocDtls": {"Typ": "INV", "No": doc.document_number, "Dt": doc.document_date},
            "SellerDtls": {"Gstin": doc.supplier_gstin},
            "BuyerDtls": {"Gstin": doc.buyer_gstin, "Pos": doc.buyer_gstin[:2]},
            "ItemList": [
                {
                    "ItemDesc": it.item_name,
                    "HsnCd": it.hsn_code,
                    "Qty": it.qty,
                    "UnitPrice": it.unit_rate,
                    "TotAmt": it.taxable_value,
                    "GstRt": it.gst_rate,
                    "CgstAmt": it.cgst_amount,
                    "SgstAmt": it.sgst_amount,
                    "IgstAmt": it.igst_amount,
                    "TotItemVal": it.total_amount,
                }
                for it in doc.items
            ],
            "ValDtls": {"TotInvVal": doc.total_invoice_value},
        }
