# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class MyStudent(models.Model):
    _name = "my.student"# name must be in lowercase or will have Value error after fixing restart service odoo to make change
    _description = "My student model"

    name = fields.Char('Student Name', required=True) #Char: text 1 dòng
    nickname = fields.Char('Nickname')
    description = fields.Text('student Description')#Text: textarea nhiều dòng
    age = fields.Integer('student Age', default=6)#Integer: số nguyên
    weight = fields.Float('Weight (kg)')#Float: số thực
    dob = fields.Date('DOB', required=False)#Date: ngày tháng năm
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', default='male')#Selection: chọn lựa, option
    student_image = fields.Binary("Student Image", attachment=True, help="Student Image")#Binary: lưu ảnh
    owner_id = fields.Many2one('res.partner', string='Owner')#Many2one: quan hệ nhiều một tới đối tượng khác: N-1
    product_ids = fields.Many2many(comodel_name='product.product',
                                string="Related Products",
                                relation='student_product_rel',
                                column1='col_student_id',
                                column2='col_product_id')#quan hệ nhiều nhiều tới đối tượng khác: N-N