from typing import Optional, List, Dict, Union

from pymongo import MongoClient
from pymongo.collection import Collection


class Database:

    user_chats: List[int] = []
    group_chats: List[int] = []
    CHAT_TACOS: Dict[int, Dict[int, Dict[str, str]]] = {}

    def __init__(self, db_url: str, name: str = None) -> 'Database':
        self.database = MongoClient(db_url)[name]
        self.on_init()

    def on_init(self):
        for u in self.database["USER_CHATS"].find():
            self.user_chats.append(u['user_id'])
        for g in self.database["GROUP_CHATS"].find():
            self.group_chats.append(g['chat_id'])
        for t in self.database["CHAT_TACOS"].find():
            if t["chat_id"] in self.CHAT_TACOS:
                self.CHAT_TACOS[t["chat_id"]].update(
                    {
                        t["user_id"]: {'name': t["name"],
                                       'username': t["username"],
                                       'tacos': t["tacos"]}
                    }
                )
            else:
                self.CHAT_TACOS[t["chat_id"]] = {
                    t["user_id"]: {'name': t["name"],
                                   'username': t["username"],
                                   'tacos': t["tacos"]}
                }

    def get_collection(self, name: str) -> Optional[Collection]:
        if self.database:
            return self.database[name]
        return None

    def add_chat(self, collection: Collection, **kwargs) -> None:
        if 'user_id' in kwargs:
            self.user_chats.append(kwargs.get('user_id', 0))
        elif 'chat_id' in kwargs:
            self.group_chats.append(kwargs.get('chat_id', 0))
        collection.insert_one(kwargs)

    def remove_chat(self, collection: Collection, **kwargs) -> None:
        if 'user_id' in kwargs:
            self.user_chats.remove(kwargs.get('user_id', 0))
        elif 'chat_id' in kwargs:
            self.group_chats.remove(kwargs.get('chat_id', 0))
        collection.delete_one(kwargs)

    def get_chats_count(self, collection: Collection) -> int:
        return collection.find().count()

    def get_top_tacos(self, chat_id: int) -> List[Dict[str, Union[str, int]]]:
        data = []
        if chat_id not in self.CHAT_TACOS:
            return data
        for a, b in self.CHAT_TACOS[chat_id].items():
            data.append({
                'user_id': a,
                'name': b.get('name', ''),
                'username': b.get('username', ''),
                'tacos': b.get('tacos')
            })
        if data:
            data.sort(key=lambda x: x["tacos"], reverse=True)
        return data[:5]

    def get_user_tacos(self,
                       chat_id: int,
                       user_id: int) -> int:
        if chat_id in self.CHAT_TACOS and user_id in self.CHAT_TACOS[chat_id]:
            return self.CHAT_TACOS[chat_id][user_id]['tacos']
        return -1

    def update_user_tacos(self,
                          chat_id: int,
                          user_id: int,
                          collection: Collection,
                          **kwargs) -> None:
        if chat_id in self.CHAT_TACOS:
            if user_id in self.CHAT_TACOS[chat_id]:
                self.CHAT_TACOS[chat_id][user_id] = kwargs
            else:
                self.CHAT_TACOS[chat_id].update({user_id: kwargs})
        else:
            self.CHAT_TACOS[chat_id] = {user_id: kwargs}
        collection.update_one({"chat_id": chat_id, "user_id": user_id},
                              {"$set": kwargs}, upsert=True)
