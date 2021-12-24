from src.domain.v1.validatore import validatore


class UserValidatore():
    def UserCreateSchema(self, data):
        return validatore(data, {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "username": {
                        "type": "string"
                    },
                    "password": {
                        "type": "string"
                    }
                },
                "required": ["username"],
                "additionalProperties": False
            }
        })

    def UserUpdateSchema(self, data):
        return validatore(data, {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "username": {
                        "type": "string"
                    },
                    "password": {
                        "type": "string"
                    }
                },
                "required": ["username"],
                "additionalProperties": False
            }
        })

    def UserDeleteSchema(self, data):
        return validatore(data, {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type_id": "objectId"
                    }
                },
                "required": ["id"],
                "additionalProperties": False
            }
        })

    def UserLoginSchema(self, data):
        return validatore(data, {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "username": {
                        "type": "string"
                    },
                    "password": {
                        "type": "string"
                    }
                },
                "required": ["username"],
                "additionalProperties": False
            }
        })

    def UserGetSchema(self, data):
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