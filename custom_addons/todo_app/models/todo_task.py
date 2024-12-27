from email.policy import default

from odoo import models, fields, api


class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(srtring='Name')
    due_date = fields.Date(string='Due Date', tracking=1)
    description = fields.Text(srtring='Description', tracking=1)
    # (tracking=1) to make this fiels display on the chatter
    assign_to = fields.Many2one('res.partner', string='Assign To', tracking=1)
    estimated_time = fields.Float(string='Estimated Time')
    task_line = fields.One2many('task.history', 'task_line_history', string='Task History')
    total_time = fields.Float(string='Total Time', compute='_compute_total_time', store=True)

    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ], default='new', string='Status', tracking=1)

    @api.depends('task_line.time')
    def _compute_total_time(self):
        """Calculate the total time from related TaskHistory records."""
        for task in self:
            task.total_time = sum(line.time for line in task.task_line)


class TaskHistory(models.Model):
    _name = 'task.history'

    task_line_history = fields.Many2one('todo.task', string='Task History')
    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    time = fields.Float(string='Time')
