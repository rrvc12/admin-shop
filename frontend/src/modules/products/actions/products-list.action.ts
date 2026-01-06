import api from '@/api/api';
import type { ProductList } from '../interfaces/product.interface';

export const productsListAction = async (page: number) => {
  try {
    const { data } = await api.get<ProductList>(`/products/products-list/?page=${page}`);

    console.log(data);

    return data;
  } catch (error) {
    console.error('Error fetching products:', error);
    throw new Error('Failed to fetch products');
  }
};
