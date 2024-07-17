/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const collection = new Collection({
    "id": "aucajdbas90ari4",
    "created": "2024-05-03 13:40:31.663Z",
    "updated": "2024-05-03 13:40:31.663Z",
    "name": "SAT",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "keqxbgtu",
        "name": "questions",
        "type": "json",
        "required": false,
        "presentable": false,
        "unique": false,
        "options": {
          "maxSize": 2000000
        }
      }
    ],
    "indexes": [],
    "listRule": null,
    "viewRule": null,
    "createRule": null,
    "updateRule": null,
    "deleteRule": null,
    "options": {}
  });

  return Dao(db).saveCollection(collection);
}, (db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("aucajdbas90ari4");

  return dao.deleteCollection(collection);
})
