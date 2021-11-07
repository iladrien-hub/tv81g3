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

