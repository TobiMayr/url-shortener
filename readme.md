# url-shortener

## Description

A simple urlshortener using django rest framework.

- Receives a URL (`originalUrl`)
- Generates a unique shortened URL (`shortUrl`)
- Returns this shortened URL
- Redirects to the original URL when accessing shortened URL
- Tracks visits in database


## Running the App

### Using Docker

`docker build -t urlshortener .`\
`docker run -p 8000:8000 urlshortener`\
The default setting is `production` use other settings (`development` or `test`) add an argument when building the docker file.\
E.g.: `docker run -p 8000:8000 urlshortener --build-arg SETTINGS=test  `

## Usage

### To shorten a URL a POST request:

#### Request:
```
curl --request POST \
  --url http://127.0.0.1:8000/urls/ \
  --header 'Content-Type: application/json' \
  --data '{
	"originalUrl": "https://example.com/long/url/that/would/need/some/shortening"
}'
```
#### Response:
```
{
	"id": "6ffe3537",
	"originalUrl": "https://example.com/long/url/that/would/need/some/shortening",
	"shortUrl": "https://tier.app/6ffe3537"
}
```

### Using a shortened URL to be redirected:

### Request:
In develop mode:
```
curl --request GET \
  --url http://127.0.0.1:8000/6ffe3537
```
In production, it should look like this:
```
curl --request GET \
  --url https://tier.app/6ffe3537
```
### Response
The server will return `HTTP/1.1 301 Moved Permanently` and then redirect to the originalUrl.

## Database

The `sqlite3` database contains two tables, `url` and `visit`,

![url table](url_table.png?raw=true "url Table")
![visit table](visit_table.png?raw=true "visit Table")

## Tests

Running the tests requires to install every dependency (I used Python 3.9):\
`sudo pip install virtualenv`\
`virtualenv venv`\
`source venv/bin/activate`\
`pip install -r requirements.txt`\
`python manage.py makemigrations --settings=urlshortener.settings.test`\
`python manage.py migrate --settings=urlshortener.settings.test`\
`./manage.py test --settings=urlshortener.settings.test`
