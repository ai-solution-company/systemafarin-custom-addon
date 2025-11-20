frappe.ui.form.on('Sales Invoice', {
    refresh(frm) {
        // دکمه تست
        frm.add_custom_button(__('Test from iran_core'), () => {
            frappe.msgprint(__('این دکمه از app iran_core اضافه شده است ✅'));
        });

        // اگر فاکتور submit شده، یک indicator سبز نشون بده
        if (frm.doc.docstatus === 1) {
            frm.set_indicator(__('Iran Core Invoice'), 'green');
        }
    }
});
