import pytest
import requests
import jsonschema
from jsonschema import validate

base_url = "https://petstore.swagger.io/v2"
pet_id = 123



def test_pet_operations():
    data = {
        "id": pet_id,
        "category": {
            "id": pet_id,
            "name": "Fluffy Ball"
        },
        "name": "Fluffy Ball",
        "photoUrls": [
            "{{$randomImageUrl}}"
        ],
        "tags": [
            {
                "id": pet_id,
                "name": "Fluffy Ball"
            }
        ],
        "status": "available"
    }

    create_pet = requests.post(f'{base_url}/pet', json = data)
    print("Create pet response: " + create_pet.text)


    update_data = {
        "id": pet_id,
        "category": {
            "id": pet_id,
            "name": "Mickey"
        },
        "name": "Mickey",
        "photoUrls": [
            "{{$randomImageUrl}}"
        ],
        "tags": [
            {
                "id": pet_id,
                "name": "Mickey"
            }
        ],
        "status": "pending"
    }

    update_pet = requests.put(f'{base_url}/pet/{pet_id}', json = update_data)
    print("Update pet response: " + update_pet.text)


    get_pet = requests.get(f'{base_url}/pet/{pet_id}')
    print("Get pet response: " + get_pet.text)

    schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "category": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer"
        },
        "name": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "name"
      ]
    },
    "name": {
      "type": "string"
    },
    "photoUrls": {
      "type": "array",
      "items": [
        {
          "type": "string"
        }
      ]
    },
    "tags": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "integer"
            },
            "name": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "name"
          ]
        }
      ]
    },
    "status": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "category",
    "name",
    "photoUrls",
    "tags",
    "status"
  ]
}
