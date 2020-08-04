import crudinical

#crudinical.initial()

#crudinical.select_all()

from user import User

user_obj = User()

print("Vamos adicionar um usuário ao banco de dados.")

user_obj.set_name(input("Digite o nome de um usuário: "))
user_obj.set_age(int(input(f"Digite a idade de {user_obj.get_name()}: ")))

crudinical.insert_one(user_obj)

crudinical.select_all()


#crudinical.delete_table()