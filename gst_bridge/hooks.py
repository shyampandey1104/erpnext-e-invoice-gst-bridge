# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "gst_bridge"
app_title = "Erpnext E Invoice Gst Bridge"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext E Invoice Gst Bridge - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/gst_bridge/css/gst_bridge.bundle.css"
app_include_js = "/assets/gst_bridge/js/gst_bridge.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Erpnext E Invoice Gst Bridge Entry": {
        "validate": "gst_bridge.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "gst_bridge.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "gst_bridge.tasks.hourly_sync"
    ],
    "daily": [
        "gst_bridge.tasks.daily_reconciliation"
    ],
    "weekly": [
        "gst_bridge.tasks.weekly_digest"
    ]
}
