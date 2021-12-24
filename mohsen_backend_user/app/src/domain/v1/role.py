from src.domain.v1.validatore import validatore


class RoleValidatore():
    def RoleCreateSchema(self, data):
        return validatore(data, {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string"
                    },
                    "permissions": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "not_allowed": {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string'
                                    }
                                },
                                "permission_id": {
                                    'type_id': 'objectId'
                                }
                            }
                        }
                    },
                    "is_assignable": {
                        "type": "boolean"
                    },
                    "is_visible": {
                        "type": "boolean"
                    },
                    "is_readonly": {
                        "type": "boolean"
                    },
                    "required": ["title"],
                    "additionalProperties": False
                }
            }
        })

    def RoleUpdateSchema(self, data):
        return validatore(data, {
            "type": "array",
            "items": {
                "properties": {
                    "title": {
                        "type": "string"
                    },
                    "permissions": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "not_allowed": {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string'
                                    }
                                },
                                "permission_id": {
                                    'type_id': 'objectId'
                                }
                            }
                        }
                    },
                    "is_assignable": {
                        "type": "boolean"
                    },
                    "is_visible": {
                        "type": "boolean"
                    },
                    "is_readonly": {
                        "type": "boolean"
                    },
                    "required": ["title"],
                    "additionalProperties": False
                }
            }
        })

    def RoleDeleteSchema(self, data):
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

    def RoleGetSchema(self, data):
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
