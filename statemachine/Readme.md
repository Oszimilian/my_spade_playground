Hey there,
im new into spade. 
I have a question about generics. Is it possible to do something like this?
```
fn all_ones<#T>() -> uint<T> {
    2^T - 1
}
```
generating a vector based on the type with all bits set to one