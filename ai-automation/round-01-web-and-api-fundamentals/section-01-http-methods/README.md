# Section 01: HTTP Methods

## Overview
This section covers the fundamentals of HTTP methods using Python and the Requests library.

## Concepts Covered
- GET: Retrieve data from an API.
- POST: Create a new resource.
- PATCH: Partially update an existing resource.
- PUT: Replace an existing resource.
- DELETE: Delete a resource.

## Tools & Technologies
- Python
- Requests Library
- DummyJSON API

## Practical Implementation
Implemented all five HTTP methods using the DummyJSON API to understand how API requests and responses work.

## Key Learnings
- Sending HTTP requests using Python.
- Working with JSON request bodies.
- Reading API responses.
- Understanding HTTP status codes.
- Understanding the difference between PUT and PATCH.

## Notes
DummyJSON simulates write operations. Changes are not permanently stored on its server.

## Status
Completed

## Important Notes

### Essential HTTP Status Codes

HTTP status codes indicate the result of an HTTP request. They help us understand whether a request was successful or encountered an error.

| Code | Meaning | Explanation |
|---|---|---|
| `200` | OK | The request was successful. |
| `201` | Created | A resource has been created. |
| `202` | Accepted | The request has been accepted for processing. |
| `204` | No Content | The request was successful, but there is no content to return. |
| `301` | Moved Permanently | The resource has been moved permanently. |
| `400` | Bad Request | The request is invalid. |
| `401` | Unauthorized | Authentication is required. |
| `403` | Forbidden | You do not have permission to access the resource. |
| `404` | Not Found | The requested resource could not be found. |
| `429` | Too Many Requests | Too many requests have been made within a given time. |
| `500` | Internal Server Error | An internal server error occurred. |
| `502` | Bad Gateway | An intermediary server received an invalid response from the upstream server. |
| `503` | Service Unavailable | The service is temporarily unavailable. |

### HTTP Status Code Classification

HTTP status codes are divided into five main categories:

| Category | Name | Explanation |
|---|---|---|
| `1xx` | Informational | Provides information regarding the request. |
| `2xx` | Success | Indicates that the request was successful. |
| `3xx` | Redirection | Further action, such as redirection, is required. |
| `4xx` | Client Errors | Indicates an issue with the request or the client's permissions. |
| `5xx` | Server Errors | Indicates an issue on the server side. |

### Important Python Note

In Python's Requests library, `response.status_code` returns the HTTP status code as an integer.

The `response.raise_for_status()` method raises an `HTTPError` exception for unsuccessful HTTP responses (4xx and 5xx status codes), helping us handle HTTP errors properly.

