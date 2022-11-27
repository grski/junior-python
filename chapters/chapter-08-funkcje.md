\pagebreak

# Funkcje

...

## Zwykłe funkcje/metody

## Argumenty funkcji

### *args, **kwargs



## Funkcje anonimowe/lambda

Tutaj będzie naprawdę krótko. Funkcje anonimowe/lambda to po prostu jednolinijkowe funkcje, którym nie nadajemy nazwy, gdyż używamy ich tylko w określonym lokalnym miejscu.

Nie jest dobrą praktyką, by ich nadużywać, natomiast w pewnych sytuacjach mają swoje zastosowanie. Zazwyczaj preferuję zwykłe funkcje, gdyż pozwalają mi bardziej rozlegle i opisowo zaznaczyć co dany kod robi. Są oczywiście trywialne przykłady i miejsca, gdzie lambdy mają sens. Warto jednak pamiętać, żeby nie tworzyć potworków, które posiadają milion zagnieżdżonych lambd czy skomplikowaną logikę.

Poniżej przykłady. 

```python
def sort_timestamp(orders):
    return sorted(orders, key=lambda x: x.timestamp)
# inny przykład
class Foo:
    def _create_transactions(
        self, 
        book_side: dict[(int, list)], 
        new_order: Order, 
        start: int = None
    ) -> Order:
        """Here we take care of creating transaction and 
        fulfilling orders if a match is found in the orderbook.
        When we process the book it's important to reverse the
        ordering based if it's a bid/ask side of orderbook.
        Orders that are fulfilled are removed from the book. 
        If no orders are present for given price
        internally it's removed from the order book. Orders that 
        are filled partly are added to the orderbook with
        the remaining quantity."""
        sorted_prices = sorted(book_side.keys(), reverse=new_order.is_ask)
        sorted_prices = sorted_prices if start is None else sorted_prices[start:]
        for price in sorted_prices:
            if new_order.is_fulfilled or new_order.price_doesnt_match(book_side_price=price):
                break

            orders_at_price: list[Order] = book_side[price]
            sorted_orders_at_price = sorted(
                orders_at_price, 
                key=lambda order: order.timestamp
            )
           	(...)
```

Do poczytania:

1. https://analityk.edu.pl/python-lambda-wszystko-co-trzeba-wiedziec/
2. https://realpython.com/python-lambda/
3. https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/
4. https://www.geeksforgeeks.org/intersection-two-arrays-python-lambda-expression-filter-function/?ref=lbp

\pagebreak

