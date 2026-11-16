# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "gst_bridge"
app_title = "Erpnext E Invoice Gst Bridge"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext E Invoice Gst Bridge for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/gst_bridge/css/gst_bridge.bundle.css"
app_include_js = "/assets/gst_bridge/js/gst_bridge.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "gst_bridge.engine.on_document_submit",
        "on_cancel": "gst_bridge.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "gst_bridge.engine.daily_scheduled_sync"
    ]
}
