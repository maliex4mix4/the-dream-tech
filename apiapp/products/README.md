# Products App

- here all info of the products app is written.
## Things to happen
- Products creation
- Product Update/delete and retrive
- Category create/update/delete and retrive


## EndPoints

**Note** All APi should follow this particular format.

**Note** All api should return in format:
`
{
  "success": #True or False,
  "payload": {
    #data goes in here.
  },
  "info": #provides additional info about the error.,
}

`
**Note** info is not necessarily sent always.

### Products
- {base_url}/api/products/  [method=POST] : add new product
- {base_url}/api/products/  [method=GET] : retrive all Products
- {base_url}/api/products/<id>  [method=get] : retrive a product
- {base_url}/api/products/<id>  [method=put] : update a product
- {base_url}/api/products/<id>  [method=delete] : deletes a product

### Category
- {base_url}/api/products/category/  [method=POST] : add new category
- {base_url}/api/products/category/  [method=GET] : retrive all categories
- {base_url}/api/products/category/<id>  [method=get] : retrive a category
- {base_url}/api/products/category/<id>  [method=put] : update a category
- {base_url}/api/products/category/<id>  [method=delete] : deletes a category
