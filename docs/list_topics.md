# List Topics

Used to list topics

**URL** : `/api/topics/`

**Method** : `GET`

**Auth required** : NO

**Data constraints**

| Parameter | Required | Default | Description |
|-----------|:--------:|:-------:|------------:|
| limit     | NO       | 15 | Number of topics requested |
| offset | NO | 0 | Number of topics requested |

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "count": 229,
    "next": "http://127.0.0.1:8000/api/v0/topics/?limit=15&offset=15",
    "previous": null,
    "results": [
        . . .
        {
            "title": "Історія розвитку інформатики"
        },
        . . .
    ]
}
```

