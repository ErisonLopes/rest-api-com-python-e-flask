from flask_restful import Resource, reqparse
from models.usuario import UserModelModel

class User(Resource):

    def get(self, user_id):
        user = UserModel.find_hotel(user_id)
        if user:
            return user.json()
        return {'message': 'User not found.'}, 404

    def delete(self, user_id):
        user = UserModel.find_hotel(user_id)
        if user:
            try:
                user.save_hotel()
            except:
                return {'message': 'An internal error ocured trying to save user.'}, 500
            return {'message': 'User deleted.'}
        return {'message': 'User not found'}, 404
