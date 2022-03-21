import frappe

from frappe.website.page_renderers.base_renderer import BaseRenderer


class FHIRRenderer(BaseRenderer):
    def can_render(self):
        if self.path.startswith('fhir/api'):
            return True

    def render(self):
        doctype = self.path.strip('/').split('/')[2]
        docs = frappe.call(frappe.client.get_list, doctype)
        data = {
            'doctype': doctype,
            'docs': docs
        }
        return self.build_response(data=data)
