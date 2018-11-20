from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash





class validator:
    def validate_empty_space(self, order):
        for k in order:
            if order[k].isspace():
                return True
        else:
            return False