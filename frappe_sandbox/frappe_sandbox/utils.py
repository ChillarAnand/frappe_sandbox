from frappe.website.page_renderers.base_renderer import BaseRenderer


class FHIRRenderer(BaseRenderer):
    def can_render(self):
        print('FHIRRenderer')
        return True

    def render(self):
        print(self.path)
        if self.path.startswith('/api/fhir'):
            return "FHIR Response"
