#!/usr/bin/env python3
"""
Marvel Comics Character Search
Python conversion of the JavaScript/HTML Marvel Comics application.
"""

import hashlib
import time
import requests
import json
import sys


class MarvelComicsAPI:
    """Client for Marvel Comics API"""
    
    def __init__(self, public_key, private_key):
        """
        Initialize Marvel Comics API client.
        
        Args:
            public_key (str): Marvel API public key
            private_key (str): Marvel API private key
        """
        self.public_key = public_key
        self.private_key = private_key
        self.base_url = "http://gateway.marvel.com/v1/public"
    
    def _generate_auth_params(self):
        """
        Generate authentication parameters for Marvel API.
        
        Returns:
            dict: Dictionary with ts, apikey, and hash parameters
        """
        # Get current timestamp in milliseconds
        timestamp = str(int(time.time() * 1000))
        
        # Create hash: md5(timestamp + private_key + public_key)
        hash_input = timestamp + self.private_key + self.public_key
        hash_value = hashlib.md5(hash_input.encode('utf-8')).hexdigest()
        
        return {
            'ts': timestamp,
            'apikey': self.public_key,
            'hash': hash_value
        }
    
    def search_comics_by_character(self, character_id):
        """
        Search for comics featuring a specific character.
        
        Args:
            character_id (str): The character ID to search for
            
        Returns:
            dict: API response data or None if error
        """
        url = f"{self.base_url}/comics"
        
        # Build request parameters
        params = self._generate_auth_params()
        params['characters'] = character_id
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from Marvel API: {e}", file=sys.stderr)
            return None
    
    def display_comics(self, data):
        """
        Display comics information in a readable format.
        
        Args:
            data (dict): Marvel API response data
        """
        if not data or 'data' not in data:
            print("No data received")
            return
        
        results = data['data'].get('results', [])
        
        if not results:
            print("No comics found for this character")
            return
        
        print("\n" + "="*80)
        print(f"TÍTULOS DONDE APARECE - Total encontrados: {len(results)}")
        print("="*80 + "\n")
        
        for idx, comic in enumerate(results, 1):
            title = comic.get('title', 'N/A')
            description = comic.get('description', 'Sin descripción disponible')
            images = comic.get('images', [])
            
            print(f"{idx}. {title}")
            print(f"   Descripción: {description}")
            
            if images:
                print(f"   Imágenes disponibles: {len(images)}")
                for img_idx, img in enumerate(images, 1):
                    img_path = img.get('path', '')
                    img_url = f"{img_path}/standard_fantastic.jpg" if img_path else 'N/A'
                    print(f"      [{img_idx}] {img_url}")
            else:
                print("   No hay imágenes disponibles")
            
            print()


def main():
    """Main function to run the Marvel Comics search"""
    
    # Marvel API credentials (same as in the original JavaScript code)
    PUBLIC_KEY = "c9b342b95e7fdb1c01efcea39f8e65e7"
    PRIVATE_KEY = "9d15e7cf75996f595ce74aa89ebc089fb19b9e34"
    
    # Get character ID from command line or prompt user
    if len(sys.argv) > 1:
        character_id = sys.argv[1]
    else:
        character_id = input("Ingrese el ID del personaje (ej: 1009368 para Iron Man): ").strip()
        
        if not character_id:
            print("Error: Debe ingresar un ID de personaje")
            sys.exit(1)
    
    # Create API client and search
    api = MarvelComicsAPI(PUBLIC_KEY, PRIVATE_KEY)
    
    print(f"\nBuscando comics para el personaje ID: {character_id}...")
    
    data = api.search_comics_by_character(character_id)
    
    if data:
        api.display_comics(data)
    else:
        print("No se pudo obtener información de la API")
        sys.exit(1)


if __name__ == "__main__":
    main()
