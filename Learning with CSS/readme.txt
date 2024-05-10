->css structure:
    1.selector.
    2.property. 
    3.value.
->Selector:
    1.Universal Selector. *
    2.Descendant selectors. ul li { }
    3.Class Selector. .className{ }
    4.Id Selector.    #idName { }
    5.Grouping Selector. selectorOne,selectorTwo { }
Desplay-:Block,FLex,----------etc.
z-index: Use to over-lab.

Measure-ment:
    1.Integer.
    2.percent.
Padding: top, right , bottom , left.
or       top-bottom, right-left.
or       *


In CSS, inheritance is a mechanism by which certain properties of an HTML element are passed down to its children elements. This means that child elements inherit specific styles from their parent elements unless explicitly overridden.

Here are some key points about inheritance in CSS:

1. **Inherited Properties**: Some CSS properties are inherited by default. This includes properties like `font-family`, `color`, `font-size`, `line-height`, `text-align`, etc. If these properties are set on a parent element, they will be inherited by its children unless overridden.

2. **Non-Inherited Properties**: Conversely, there are properties that are not inherited by default. These include properties like `border`, `margin`, `padding`, `width`, `height`, etc. Child elements do not inherit these properties from their parent elements.

3. **Forced Inheritance**: You can force inheritance of non-inherited properties using the `inherit` keyword. For example, if you want a child element to inherit the `color` property from its parent, you can explicitly set it to `inherit`.

4. **Cascading**: Inheritance is part of the broader concept of cascading in CSS. The cascade determines how styles are applied when multiple conflicting styles are present. Inherited styles are resolved as part of this cascade.

5. **Override**: Child elements can override inherited styles by applying their own styles. This allows for fine-grained control over the appearance of individual elements.

6. **Performance**: While inheritance can simplify styling in some cases, it can also lead to unintended consequences and performance issues if not used carefully. Inherited styles can propagate through the entire DOM tree, potentially causing unnecessary computation.

Here's an example to illustrate inheritance in CSS:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inheritance Example</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            color: #333;
        }

        h1 {
            font-size: 24px;
            color: blue;
        }

        p {
            font-size: 16px;
        }
    </style>
</head>
<body>
    <h1>This is a heading</h1>
    <p>This is a paragraph.</p>
    <div>
        <h1>This is a heading inside a div</h1>
        <p>This is a paragraph inside a div.</p>
    </div>
</body>
</html>
```

In this example:
- The `body` element sets `font-family` and `color`, which are inherited by all child elements.
- The `h1` element sets its own `font-size` and overrides the `color` inherited from the `body`.
- The `p` element sets its own `font-size`.
- When the `h1` and `p` elements are placed inside a `div`, they still inherit the `font-family` and `color` from the `body`, but the `h1` element's `font-size` is inherited from its own style, not from the `body`.

->In_Line CSS.
->External CSS.
->Internal CSS.
->Different Type of Cursor.
->Gride:
    -Es a two-dimensional layout. 
    -We can arrage elemnt in row-column.
    -Responsive Design.
    -Easy to maintance.
    -gride can compress his own size.
-Flex: 
    -One dimensional layout.
font:
    -font family 
    -font weight