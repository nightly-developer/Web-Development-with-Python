
import os
from supabase import create_client, Client

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def fetch_all_products():
  data, _ = supabase.from_('product').select('name').execute()
  return data[1]
