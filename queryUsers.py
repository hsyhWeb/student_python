from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
from flask import Flask, request, jsonify
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/people?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(
    app,
    origins=["http://localhost:5173"],  # 必须明确指定来源，不能用 "*"
    supports_credentials=True           # 允许携带凭据（如 Cookies）
)
# 用户模型
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10))
    role = db.Column(db.String(20))
    status = db.Column(db.Integer, default=1)  # 1 表示可用


AVATAR_FOLDER = 'avatar'
os.makedirs(AVATAR_FOLDER, exist_ok=True)
# 注册接口
@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    gender = request.form.get('gender')
    role = request.form.get('role')
    avatar = request.files.get('avatar')

    # 用户名重复检查
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists', 'status': 401}), 401

    # 保存头像
    avatar_filename = None
    if avatar:
        ext = os.path.splitext(secure_filename(avatar.filename))[-1]  # 获取扩展名
        avatar_filename = f"{username}_avatar{ext}"
        avatar_path = os.path.join(AVATAR_FOLDER, avatar_filename)
        avatar.save(avatar_path)

    # 创建用户（status 默认设置为 active）
    new_user = User(
        username=username,
        password=password,
        gender=gender,
        role=role,
        status='active'
        # 可以扩展头像字段保存路径，例如 avatar_path=avatar_filename
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Registration successful', 'status': 200}), 201

# 登录接口
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username, password=password).first()
    if user and user.status == 'active':
        user_data = {
            'id': user.id,
            'username': user.username,
            'password': user.password,
            'gender': user.gender,
            'role': user.role,
            'status': user.status
        }
        return jsonify({'message': 'Login successful', 'status': '200', 'user': user_data}), 200
    else:
        return jsonify({'message': 'Invalid credentials or user disabled', 'status': '401'}), 401

@app.route('/update_user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found', 'status': '404'}), 404

    data = request.json
    # 只更新提供的字段
    if 'username' in data:
        user.username = data['username']
    if 'password' in data:
        user.password = data['password']
    if 'gender' in data:
        user.gender = data['gender']
    if 'role' in data:
        user.role = data['role']
    if 'status' in data:
        user.status = data['status']

    db.session.commit()
    return jsonify({'message': 'User updated successfully', 'status': '200'}), 200


from flask import send_from_directory, abort


@app.route('/avatar/<username>', methods=['GET'])
def get_avatar(username):
    avatar_folder = 'avatar'

    # 遍历 avatar 目录查找对应用户名头像
    for filename in os.listdir(avatar_folder):
        if filename.startswith(f"{username}_avatar"):
            return send_from_directory(avatar_folder, filename)

    # 没有找到则返回 404
    return jsonify({'message': 'Avatar not found', 'status': 404}), 404


# 启动服务
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # 确保表存在
    app.run(debug=True)
