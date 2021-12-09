# -*- coding: utf-8 -*-
from odoo import models, fields, api

class PlayerSummary(models.Model):
    _name = 'player.summary'
    _description = 'Player Summary'
    _order = 'name'

    @api.depends('name','runs','wickets')
    def _calculate_average(self):
        for record in self:
            record['batting_average']= round((record.runs / (record.name or 1.0)),2)
            record['bowling_average']= round((record.wickets / (record.name or 1.0)),2)

    name = fields.Integer(string='Matches Played')
    player_id = fields.Many2one('player.player')
    cricket_format = fields.Selection(
        [('test', 'Test'),
         ('odi', 'ODI'),
         ('t20', 'T20'),
         ('t10', 'T10'),
        ], string='Cricket Format',
        help="Please choose....")
    runs = fields.Integer(string='Runs')
    highest_runs = fields.Integer(string='Highest Runs')
    wickets = fields.Integer(string='Wickets')
    best_wicket_figure = fields.Integer(string='Best Figure Wkts')
    won = fields.Integer(string='Won')
    loss = fields.Integer(string='Loss')
    draw = fields.Integer(string='Draw')
    batting_average = fields.Float(string='Batting Avg', compute="_calculate_average", store=True)
    bowling_average = fields.Float(string='Bowling Avg', compute="_calculate_average", store=True)

class TeamList(models.Model):
    _name = 'team.list'
    _description = 'Team List'
    _order = 'name'

    name = fields.Char(string='Name')

class Player(models.Model):
    _name = 'player.player'
    _inherit = "res.partner"

    birth_place = fields.Char(string='Birth Place')
    height = fields.Char(string='Height')
    ranking = fields.Char(string='Rankings')
    
    birth_date = fields.Date(string='Born')
    
    about_player = fields.Text(string='About Player')
    description = fields.Text()
    
    team_id = fields.Many2one('team.list', string='Team')
    
    player_summary_line = fields.One2many('player.summary', 'player_id', string='Batting Summary')
    
    role = fields.Selection(
        [('batsman', 'Batsman'),
         ('bowler', 'Bowler'),
         ('batting allrounder', 'Batting Allrounder'),
         ('bowling allrounder', 'Bowling Allrounder'),
        ], string='Role',
        help="Please select role from list.")
    batting_style = fields.Selection(
        [('right handed bat', 'Right Handed Bat'),
         ('left handed bat', 'Left Handed Bat'),
        ], string='Batting Style',
        help="Please select batting style from list.")
    bowling_style = fields.Selection(
        [('right-arm fast', 'Right-arm fast'),
         ('right-arm fast-medium', 'Right-arm fast-medium'),
         ('right-arm fast-medium', 'Right-arm fast-medium'),
         ('left-arm fast', 'Left-arm fast'),
         ('left-arm fast-medium', 'Left-arm fast-medium'),
         ('right-arm offbreak', 'Right-arm offbreak'),
         ('right-arm legbreak', 'Right-arm legbreak'),
         ('left-arm orthodox', 'Left-arm orthodox'),
        ], string='Bowling Style',
        help="Please select bowling style from list.")
        
    matches_won = fields.Integer(compute="_calculate_matches_result", store=True)
    matches_loss = fields.Integer(compute="_calculate_matches_result", store=True)
    matches_draw = fields.Integer(compute="_calculate_matches_result", store=True)
    
    @api.depends('player_summary_line.won','player_summary_line.loss','player_summary_line.draw')
    def _calculate_matches_result(self):
        for record in self:
            record['matches_won']=sum([l.won for l in record.player_summary_line])
            record['matches_loss']=sum([l.loss for l in record.player_summary_line])
            record['matches_draw']=sum([l.draw for l in record.player_summary_line])
            