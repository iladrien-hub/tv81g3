# List Topics

Used to list topics

**URL** : `/api/v0/topics/`

**Method** : `GET`

**Auth required** : NO

**Data constraints**

| Parameter | Required | Default | Description |
|-----------|:--------:|:-------:|:------------|
| limit     | NO       | 15 | Number of topics requested |
| offset | NO | 0 | The number of the first topic in the list |
| title | NO | None | Used to filter topics by title. Case insensitively. |
| year | NO | None | Used to filter topics by year. |
| director | NO | None | Used to filter topics by scientific director's name. <br/> __Note__: The algorithm uses a fuzzy comparison approach. Thus, word order and minor spelling errors do not matter. |

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
  "count": 229,
  "next": "http://tv81bachelours.pythonanywhere.com/api/v0/topics/?limit=15&offset=30",
  "previous": "http://tv81bachelours.pythonanywhere.com/api/v0/topics/?limit=15",
  "results": [
    {
      "pk": 1491,
      "title": "Інформаційна основа управління економікою",
      "year": 2011,
      "director": {
        "pk": 95,
        "last_name": "Князєва",
        "first_name": "Уляна",
        "patronymic": "Тимофіївна"
      },
      "students": [
        {
          "pk": 2060,
          "last_name": "Філімонов",
          "first_name": "Мирослав",
          "patronymic": "Гордійович"
        }
      ]
    }
  ]
}
```

## Error Response

**Condition** : If year is not a valid integer value.

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "year": "Value \"2020ads\" can't be interpreted as integer."
}
```
