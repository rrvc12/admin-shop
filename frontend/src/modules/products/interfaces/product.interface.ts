export interface Product {
  id: number;
  name: string;
  image_url: string | null;
  slug: string;
  sale_price: string;
}

export interface ProductList {
  count: number;
  next: string | null;
  previous: string | null;
  results: Product[];
  num_pages: number;
}
