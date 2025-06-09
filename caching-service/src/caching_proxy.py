import argparse
import requests
import json
from flask import Flask, request, Response
from cachetools import TTLCache

# Crear caché con TTL
cache = TTLCache(maxsize=100, ttl=300)

def build_response(body, status_code, headers, from_cache=False):
    response = Response(body, status_code, headers)
    response.headers['X-Cache'] = 'HIT' if from_cache else 'MISS'
    print(response.headers['X-Cache'])
    return response

def proxy_handler(origin, path):
    cache_key = request.full_path

    if cache_key in cache:
        body, status_code, headers = cache[cache_key]
        return build_response(body, status_code, headers, from_cache=True)

    try:
        url = f'{origin}/{path}'
        upstream_response = requests.get(url, params=request.args)
        
        body = upstream_response.content
        print(body)
        status_code = upstream_response.status_code
        headers = dict(upstream_response.headers)

        # Guardar en cache como tupla
        cache[cache_key] = (body, status_code, headers)

        return build_response(body, status_code, headers, from_cache=False)

    except requests.RequestException as e:
        print(f"[ERROR] Failed to fetch from origin: {e}")
        return Response("Upstream error", status=502)

def start_server(port, origin):
    app = Flask(__name__)

    @app.route('/', defaults={'path': ''}, methods=['GET'])
    @app.route('/<path:path>', methods=['GET'])
    def proxy(path):
        return proxy_handler(origin, path)

    app.run(port=port)

def clear_cache():
    cache.clear()
    print("Cache removed")

def main(): 
    parser = argparse.ArgumentParser(description="Caching Reverse Proxy")
    parser.add_argument('--port', type=int, help='Port to run the Flask server on')
    parser.add_argument('--origin', type=str, help='Origin server URL to proxy requests to')
    parser.add_argument('--clear-cache', action="store_true", help='Clear the cache and exit')

    args = parser.parse_args()

    if args.clear_cache:
        clear_cache()
        return

    if args.port is None or args.origin is None:
        parser.error("--port and --origin are required unless --clear-cache is used")


    start_server(args.port, args.origin)

if __name__ == "__main__":
    main()