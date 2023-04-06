# WEATHER APP :cloud:

A simple weather app developed in Python's framework **'DJANGO'** that shows the weather in realtime and forecasts 3 days ahead all by making use of an API.

## API Reference

**Base url** : http://api.weatherapi.com/v1

#### Get all items

```http
  GET /forecast.json or /forecast.xml
```

| Parameter | Type     | Description                                                     |
| :-------- | :------- | :-------------------------------------------------------------- |
| `key`     | `string` | **Required**. Your API key                                      |
| `q`       | `string` | **Required**. Query parameter based on which data is sent back. |
| `days`    | `int`    | **Required**. Number of days of forecast required.              |
