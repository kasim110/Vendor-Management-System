# Vendor Management System

## Overview

This Django project implements a Vendor Management System (VMS) with RESTful APIs to manage vendors, purchase orders, and vendor performance metrics.

## API Endpoints

### Vendor Management Endpoints

#### Create a new vendor
- Endpoint: `POST /api/vendors/`
- Description: Create a new vendor.
- Request Body:
    ```json
    {
        "name": "Vendor X",
        "contact_details": "1234567890",
        "address": "123 Main St",
        "vendor_code": "VEND123"
    }
    ```
- Response: Returns details of the created vendor.

#### Retrieve all vendors
- Endpoint: `GET /api/vendors/`
- Description: Retrieve a list of all vendors.

#### Retrieve a specific vendor
- Endpoint: `GET /api/vendors/{vendor_id}/`
- Description: Retrieve details of a specific vendor identified by vendor_id.

#### Update a vendor
- Endpoint: `PUT /api/vendors/{vendor_id}/`
- Description: Update details of a specific vendor identified by vendor_id.
- Request Body: Provide JSON data with fields to update.

#### Delete a vendor
- Endpoint: `DELETE /api/vendors/{vendor_id}/`
- Description: Delete a specific vendor identified by vendor_id.

### Purchase Order Tracking Endpoints

#### Create a new purchase order
- Endpoint: `POST /api/purchase_orders/`
- Description: Create a new purchase order.
- Request Body:
    ```json
    {
        "po_number": "PO123",
        "vendor": 1,
        "order_date": "2024-04-30T00:00:00Z",
        "delivery_date": "2024-05-07T00:00:00Z",
        "items": [{"item_name": "Product A", "quantity": 5}],
        "quantity": 5,
        "status": "pending"
    }
    ```
- Response: Returns details of the created purchase order.

#### Retrieve all purchase orders
- Endpoint: `GET /api/purchase_orders/`
- Description: Retrieve a list of all purchase orders.

#### Retrieve a specific purchase order
- Endpoint: `GET /api/purchase_orders/{po_id}/`
- Description: Retrieve details of a specific purchase order identified by po_id.

#### Update a purchase order
- Endpoint: `PUT /api/purchase_orders/{po_id}/`
- Description: Update details of a specific purchase order identified by po_id.
- Request Body: Provide JSON data with fields to update.

#### Delete a purchase order
- Endpoint: `DELETE /api/purchase_orders/{po_id}/`
- Description: Delete a specific purchase order identified by po_id.

### Vendor Performance Evaluation

#### Retrieve a vendor's performance metrics
- Endpoint: `GET /api/vendors/{vendor_id}/performance/`
- Description: Retrieve calculated performance metrics for a specific vendor.
- Response: Returns data including on_time_delivery_rate, quality_rating_avg, average_response_time, and fulfillment_rate.

#### Acknowledgment of purchase order by vendor
- Endpoint: `POST /api/purchase_orders/{po_id}/acknowledge/`
- Description: Endpoint for vendors to acknowledge purchase orders.
- Response: Updates acknowledgment_date and triggers recalculation of average_response_time.



## Running the Project

1. Install required packages: `pip install -r requirements.txt`
2. Apply migrations: `python manage.py migrate`
3. Start the development server: `python manage.py runserver`

## Usage

- Use API client tools like Postman or cURL to interact with the implemented endpoints.