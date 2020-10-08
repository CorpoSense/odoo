# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models
import logging

log = logging.getLogger(__name__)

class FichePayeParser(models.AbstractModel):
    _name = 'report.l10n_dz_hr_payroll.report_l10ndzfichepaye'

    def get_payslip_lines(self, objs):
        res = []
        ids = []
        for item in objs:
            if item.appears_on_payslip is True and not item.salary_rule_id.parent_rule_id and item.code != 'R999':
                ids.append(item.id)
        if ids:
            res = self.env['hr.payslip.line'].browse(ids)
        return res

    def get_total_by_rule_category(self, obj, code):
        category_total = 0
        category_id = self.env['hr.salary.rule.category'].search([('code', '=', code)], limit=1).id
        if category_id:
            line_ids = self.env['hr.payslip.line'].search([('slip_id', '=', obj.id), ('category_id', 'child_of', category_id)])
            for line in line_ids:
                category_total += line.total
        return category_total

    def get_employer_line(self, obj, parent_line):
        return self.env['hr.payslip.line'].search([('slip_id', '=', obj.id), ('salary_rule_id.parent_rule_id.id', '=', parent_line.salary_rule_id.id)], limit=1)

    @api.model
    def get_report_values(self, docids, data=None):
        self.model = self.env.context.get("active_model")
        if data is None:
            data = {}
        payslip = self.env['hr.payslip'].browse(docids)
        return {
            "doc_ids": docids,
            "doc_model": self.model,
            "docs": payslip,
            "data": data,
            'get_payslip_lines': self.get_payslip_lines,
            'get_total_by_rule_category': self.get_total_by_rule_category,
            'get_employer_line': self.get_employer_line,
        }
