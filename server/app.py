from flask import Flask, request, session, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, User, Workout

app = Flask(__name__)
app.secret_key = b'\x17\x02\x04\x0b\xf6\x83\x12\x0b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)

class Signup(Resource):
    def post(self):
        data = request.get_json()
        try:
            user = User(username=data.get('username'))
            user.password_hash = data.get('password')
            db.session.add(user)
            db.session.commit()
            session['user_id'] = user.id
            return make_response(user.to_dict(), 201)
        except Exception:
            return make_response({"error": "Unprocessable Entity"}, 422)

class Login(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data.get('username')).first()
        if user and user.authenticate(data.get('password')):
            session['user_id'] = user.id
            return make_response(user.to_dict(), 200)
        return make_response({"error": "Unauthorized"}, 401)

class CheckSession(Resource):
    def get(self):
        user = User.query.filter_by(id=session.get('user_id')).first()
        if user:
            return make_response(user.to_dict(), 200)
        return make_response({"error": "Unauthorized"}, 401)

class Logout(Resource):
    def delete(self):
        session['user_id'] = None
        return make_response({}, 204)

class Workouts(Resource):
    def get(self):
        u_id = session.get('user_id')
        if not u_id:
            return make_response({"error": "Unauthorized"}, 401)
        
        # Pagination requirement
        page = request.args.get('page', 1, type=int)
        workouts_query = Workout.query.filter_by(user_id=u_id).paginate(page=page, per_page=5)
        return make_response([w.to_dict() for w in workouts_query.items], 200)

    def post(self):
        u_id = session.get('user_id')
        if not u_id:
            return make_response({"error": "Unauthorized"}, 401)
        data = request.get_json()
        workout = Workout(title=data['title'], notes=data.get('notes'), user_id=u_id)
        db.session.add(workout)
        db.session.commit()
        return make_response(workout.to_dict(), 201)

api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(CheckSession, '/check_session')
api.add_resource(Workouts, '/workouts')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
