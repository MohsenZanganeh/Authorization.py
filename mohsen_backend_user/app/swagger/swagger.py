import os
from dotenv import load_dotenv
load_dotenv('.env', verbose=True)
SERVER_URL = os.getenv('SERVER_URL')

swagger = {
    "openapi": "3.0.0",
    "info": {
        "version": "1.0.0",
        "title": "User",
        "contact": 'null',
        "description": 'Apis'
        f'''
       <a href="http://{SERVER_URL}:5002/api/docs">User Service</a>
       <a href="http://{SERVER_URL}:5003/api/docs">Product Service</a>
       <a href="http://{SERVER_URL}:5004/api/docs">Fs Service</a>
       '''
    },
    "tags": [
        {
            "name": "user",
        },
        {
            "name": "Permission",
        },
        {
            "name": "Role",
        }
    ],
    "components": {
        "securitySchemes": {
            "bearerAuth": {
                "type": "http",
                "scheme": "bearer",
                "in": "header"
            }
        }
    },
    "paths": {
        "/user/login": {
            "post": {
                "summary": "Login User",
                "tags": [
                    'user'
                ],
                "consumes": [
                    "application/json"
                ],
                "is_generic": True,
                "is_public": True,
                "requestBody": {
                    "content": {
                        "application/json": {
                            "examples": {
                                "superAdminUser": {
                                    "value": {
                                        "username": "superadmin",
                                        "password": "123"
                                    }
                                }
                            },
                            "schema": {
                                "type": "object",
                                "required": [
                                    "username"
                                ],
                                "properties": {
                                    "username": {
                                        "type": "string"
                                    },
                                    "password": {
                                        "type": "string"
                                    }
                                }
                            }
                        }
                    }
                },
                "responses": {
                    "201": {
                        "description": "Created"
                    }
                }
            }
        },
        "/user/register": {
            "post": {
                "summary": "register User",
                "tags": [
                    'user'
                ],
                "consumes": [
                    "application/json"
                ],
                "is_generic": True,
                "is_public": True,
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "required": [
                                    "username"
                                ],
                                "properties": {
                                    "username": {
                                        "type": "string"
                                    },
                                    "password": {
                                        "type": "string"
                                    }
                                }
                            }
                        }
                    }
                },
                "responses": {
                    "201": {
                        "description": "Created"
                    }
                }
            }
        },
        "/user/logout": {
            "put": {
                "consumes": [
                    "application/json"
                ],
                "is_generic": True,
                "summary": "logout User",
                "tags": [
                    'user'
                ],
                "parameters": [
                    {
                        "in": "query",
                        "name": "offset",
                        "schema": {
                            "type": "integer"
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "signed out"
                    }
                }
            }
        },
        "/user/{id}": {
            "put": {
                "consumes": [
                    "application/json"
                ],
                "is_generic": True,
                "summary": "update User",
                "tags": [
                    'user'
                ],
                "parameters": [
                    {
                        "in": "path",
                        "name": "id",
                        "description": "id of Role",
                        "schema": {
                            "type": "string",
                            "required": [
                                "id"
                            ]
                        }
                    }
                ],
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "required": [
                                    "username"
                                ],
                                "properties": {
                                    "username": {
                                        "type": "string"
                                    },
                                    "password": {
                                        "type": "string"
                                    }
                                }
                            }
                        }
                    }
                },
                "responses": {
                    "201": {
                        "description": "updated user"
                    }
                }
            },
            "get": {
                "consumes": [
                    "application/json"
                ],
                "is_generic": True,
                "summary": "get a User",
                "tags": [
                    'user'
                ],
                "parameters": [
                    {
                        "in": "path",
                        "name": "id",
                        "schema": {
                            "type": "string"
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "signed out"
                    }
                }
            }
        },
        "/user": {
            "get": {
                "consumes": [
                    "application/json"
                ],
                "is_generic": True,
                "summary": "get a User",
                "tags": [
                    'user'
                ],
                "responses": {
                    "201": {
                        "description": "signed out"
                    }
                }
            }
        },
        "/role/": {
            "post": {
                "summary": "Create Role",
                "consumes": [
                    "application/json"
                ],
                "tags": [
                    'Role'
                ],
                "is_admin": True,
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "required": [
                                    "title"
                                ],
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
                                                    "type": "string"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "responses": {
                    "201": {
                        "description": "Role Created"
                    }
                }
            },
            "get": {
                "summary": "Get All Role Type",
                "consumes": [
                    "application/json"
                ],
                "is_admin": True,
                "tags": [
                    'Role'
                ],
                "responses": {
                    "201": {
                        "description": "Got All Role"
                    }
                }
            }
        },
        "/role/{id}": {
            "put": {
                "summary": "Update Role",
                "consumes": [
                    "application/json"
                ],
                "is_admin": True,
                "tags": [
                    'Role'
                ],
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "required": [
                                    "title"
                                ],
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
                                                    "type": "string"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "parameters": [
                    {
                        "in": "path",
                        "name": "id",
                        "description": "id of Role",
                        "schema": {
                            "type": "string",
                            "required": [
                                "id"
                            ]
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "Role Updated"
                    }
                }
            },
            "get": {
                "summary": "Get One Role",
                "consumes": [
                    "application/json"
                ],
                "is_admin": True,
                "tags": [
                    'Role'
                ],
                "parameters": [
                    {
                        "in": "path",
                        "name": "id",
                        "description": "id of Role",
                        "schema": {
                            "type": "string",
                            "required": [
                                "id"
                            ]
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Got a Role"
                    }
                }
            },
            "delete": {
                "summary": "Delete A Role",
                "consumes": [
                    "application/json"
                ],
                "is_admin": True,
                "tags": [
                    'Role'
                ],
                "parameters": [
                    {
                        "in": "path",
                        "name": "id",
                        "schema": {
                            "type": "string",
                            "required": [
                                "id"
                            ]
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "Role Deleted"
                    }
                }
            }
        },
        "/permission/": {
            "get": {
                "summary": "Get All Permission Type",
                "consumes": [
                    "application/json"
                ],
                "is_admin": True,
                "tags": [
                    'Permission'
                ],
                "responses": {
                    "201": {
                        "description": "Got All Permission"
                    }
                }
            }
        },
        "/permission/{id}": {
            # "put": {
            #     "summary": "Update Permission",
            #     "consumes": [
            #         "application/json"
            #     ],
            #     "tags": [
            #         'Permission'
            #     ],
            #     "is_admin": True,
            #     "requestBody": {
            #         "content": {
            #             "application/json": {
            #             "schema": {
            #                 "type": "object",
            #                 "required": [
            #                     "title"
            #                 ],
            #                 "properties": {
            #                     "title": {
            #                         "type": "string"
            #                     },
            #                     "group": {
            #                         "type": "string"
            #                     },
            #                     "path": {
            #                         "type": "string"
            #                     },
            #                     "method": {
            #                         "type": "string"
            #                     },
            #                     "is_admin": {
            #                         "type": "boolean"
            #                     },
            #                     "is_generic": {
            #                         "type": "boolean"
            #                     },
            #                     "is_public": {
            #                         "type": "boolean"
            #                     }
            #                 }
            #             }
            #             }
            #         }
            #     },
            #     "parameters": [
            #         {
            #             "in": "path",
            #             "name": "id",
            #             "description": "id of Permission",
            #             "schema": {
            #                 "type": "string",
            #                 "required": [
            #                     "id"
            #                 ]
            #             }
            #         }
            #     ],
            #     "responses": {
            #         "201": {
            #             "description": "Permission Updated"
            #         }
            #     }
            # },
            "get": {
                "summary": "Get One Permission",
                "consumes": [
                    "application/json"
                ],
                "is_admin": True,
                "tags": [
                    'Permission'
                ],
                "parameters": [
                    {
                        "in": "path",
                        "name": "id",
                        "description": "id of Permission",
                        "schema": {
                            "type": "string",
                            "required": [
                                "id"
                            ]
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Got a Permission"
                    }
                }
            },
            # "delete": {
            #     "summary": "Delete A Permission",
            #     "consumes": [
            #         "application/json"
            #     ],
            #     "is_admin": True,
            #     "tags": [
            #         'Permission'
            #     ],
            #     "parameters": [
            #         {
            #             "in": "path",
            #             "name": "id",
            #             "schema": {
            #                 "type": "string",
            #                 "required": [
            #                     "id"
            #                 ]
            #             }
            #         }
            #     ],
            #     "responses": {
            #         "201": {
            #             "description": "Permission Deleted"
            #         }
            #     }
            # }
        }
    }
}


def generate_swagger(swagger):
    for path in swagger['paths']:
        methods = swagger['paths'][path]
        for method in methods:
            is_public = methods[method].get('is_public')
            if is_public == None or is_public == False:
                methods[method]['security'] = [{'bearerAuth': []}]
    return swagger


generated_swagger = generate_swagger(swagger)
