from src.domain.v1.validatore import validatore


class PermissionValidatore():
    def PermissionCreateSchema(self, data):
        return validatore(data, {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string"
                    },
                    "routes_id": {
                        "type": "array",
                        "items": {
                            "type_id": 'objectId'
                        }
                    },
                    'group': {
                        "type": "string"
                    },
                    "is_generic": {
                        "type": "boolean"
                    },
                    "is_public": {
                        "type": "boolean"
                    },
                },
                "required": ["title"],
                "additionalProperties": False
            }
        })

    def PermissionUpdateSchema(self, data):
        return validatore(data, {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string"
                    },
                    "routes_id": {
                        "type": "array",
                        "items": {
                            "type": 'objectId'
                        }
                    },
                    'group': {
                        "type": "string"
                    },
                    "is_generic": {
                        "type": "boolean"
                    },
                    "is_public": {
                        "type": "boolean"
                    },
                },
                "required": ["title"],
                "additionalProperties": False
            }
        })

    def PermissionGetSchema(self, data):
            return validatore(data, {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "_id": {
                            "type_id": "objectId"
                        }
                    },
                    "required": ["_id"],
                    "additionalProperties": False
                }
            })
    def PermissionDeleteSchema(self, data):
            return validatore(data, {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "_id": {
                            "type_id": "objectId"
                        }
                    },
                    "required": ["_id"],
                    "additionalProperties": False
                }
            })