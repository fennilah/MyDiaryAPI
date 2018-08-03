# from flask import Flask, jsonify,request
# import os
# import psycopg2
# from flask import Flask, jsonify, request
# from flask_jwt_extended import (JWTManager, create_access_token)


# # # app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET')
# # jwt = JWTManager(app)

# class Diary:
#     def __init__(self):
#         self.entries = []
#         self.db=conn.db_return()
        
#     def signup(self, user_data):
#         user = request.get_json()
#         name = (user['name'])
#         cur.execute("SELECT * FROM users WHERE name = %s", (name,))
#         name_data = cur.fetchall()
#         if not name_data:
#             cur.execute("""INSERT INTO users (name, password, email)
#                                 VALUES (%(name)s, %(password)s, %(email)s)""", user_data)
#             self.conn.commit()
#             return jsonify({'message': 'User created successfully'}), 201
#         return jsonify({'message': 'Name already exists'}), 400
        
#     def login(self, name, password):
#         credentials = request.get_json()
#         password = (credentials['password'])
#         name = (credentials['name'])

#         cursor.execute("""SELECT password, name FROM users WHERE name = (%s)""")
#         data = cursor.fetchone(name_data)
#         if not data[2] == name:
#             return jsonify({'message': 'Name is invalid'}), 400
#             if data[1] == password:
#                 access_token = create_access_token(identity=name)
#                 return jsonify({'token': access_token, 'message': 'Login successful'}), 200
#             else:
#                 return jsonify({'message': 'password is invalid'}), 400
        
#     def all_diary_entries(self, ):
#         cur = self.db.cursor()
#         cur.execute("SELECT * FROM entries")
#         all_diary_entries = []
        
#         for diary_entries in diary_entries:
#             single_entry = {}
#             single_entry["id of the entry"] = diary_entries[1]
#             single_entry["title of the entry"] = diary_entries[2]
#             single_entry["date_created"] = diary_entries[3]
#             single_entry["description of the entry"] = diary_entries[4]
#             all_diary_entries.append()
#             return jsonify({'message': 'Entries created successfully'}), 201
#         return jsonify({'message': 'Entry already exists'}), 400  

#     def delete_diary_entries(self, ):
#         cur = self.db.cursor()
#         cur.execute("SELECT * FROM entries")
#         delete_diary_entries = []
        
#         for diary_entries in diary_entries:
#             single_entry = {}
#             single_entry["id of the deleted entry"] = diary_entries[1]
#             single_entry["title of the deleted entry"] = diary_entries[2]
#             single_entry["date_deleted"] = diary_entries[3]
#             delete_diary_entries.append()
#             return jsonify({'message': 'Entries deleted successfully'}), 201
#         return jsonify({'message': 'Entry already deleted'}), 400  

