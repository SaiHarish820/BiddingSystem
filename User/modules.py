from flask import Flask, render_template, request
class User:
    def register(self):
        user_reg = {
            "username" : request.form.get('run'),
            "Company Name" : request.form.get('rcn'),
            "Email" : request.form.get('rem'),
            "Password" : request.form.get('rpd')
            }
        return user_reg
        