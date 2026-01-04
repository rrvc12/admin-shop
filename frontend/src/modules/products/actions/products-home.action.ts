import api from '@/api/api';
import type { Product } from '../interfaces/product.interface';

export const productsHomeAction = async () => {
  try {
    const { data } = await api.get<Product[]>('/products/products-home/');

    console.log(data);

    return data;
  } catch (error) {
    console.error('Error fetching products:', error);
    throw new Error('Failed to fetch products');
  }
};
