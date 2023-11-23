
# Vendor Management System

This system will handle vendor profiles, track purchase orders, and calculate vendor performance metrics. This project has multiple api which can be user to fetch the data.

## Project setup

In your system python version should be above 3.0 version
Django admin should be installed if it is not there then run 

```bash
  pip install django
```
After that pull the project in your local system

Install django rest framework on your system if it is not installed

```bash
  pip install djangorestframework
```
To migrate all the database changes 

```bash
  python manage.py makemigrations
  python manage.py migrate
```
Create super user 

```bash
  python manage.py createsuperuser
```
After that is will ask for some information like name, email, password 

To run the server use 

```bash
  python manage.py runserver
```
To access admin panel on your browser goto 

```bash
  127.0.0.1:8000/admin/
```
## API Reference

#### post vendor details

```http
  POST /api/vendors/
```

#### Get all vendor details

```http
  GET /api/vendors/
```

#### Get specific vendor details

```http
  GET /api/vendors/{vendor_id}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `vendor_id`      | `int` | **Required**. Id of vendor to fetch |


#### Put specific vendor details

```http
  PUT /api/vendors/{vendor_id}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `vendor_id`      | `int` | **Required**. Id of vendor to put |

#### Delete specific purchase orders

```http
  DELETE /api/vendors/{vendor_id}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `vendor_id`      | `int` | **Required**. Id of vendor to delete |


#### post purchase orders

```http
  POST /api/purchase_orders/
```


#### Get all purchase orders

```http
  GET /api/purchase_orders/
```


#### Get specific purchase orders

```http
  GET /api/purchase_orders/{po_id}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `po_id`      | `int` | **Required**. Id of item to fetch |


#### Put specific purchase orders

```http
  PUT /api/purchase_orders/{po_id}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `po_id`      | `int` | **Required**. Id of item to put |

#### Delete specific purchase orders

```http
  DELETE /api/purchase_orders/{po_id}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `po_id`      | `int` | **Required**. Id of item to delete |


#### Get specific vendor's performance histroy

```http
  GET /api/vendors/{vendor_id}/performance
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `vendor_id`      | `int` | **Required**. Id of vendor to fetch |



## Authors

- [@Radheshyam Jha](https://www.github.com/Radhe2001)

