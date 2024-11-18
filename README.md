First of all in the console navigate to the folder containing requirements.txt and run the command  ```pip install -r requirements.txt```

Ensure the clui folder is in the same directory as your Python script. This allows you to import the module without any issues.
```
/my_project
    ├── your_script.py
    └── clui
        ├── index.py
        └── utils
```

At the beginning of your Python file, import the clui.index module
```
import clui.index as cli
```

To create ASCII art from text, use the ascii function. You can specify different fonts to customize the output.
```
ascii_art = cli.ascii("Welcome", font='banner')
print(ascii_art)
```

for more fonts for the ascii function use:
```
print(cli.ascii_fonts)
```

The fadet function allows you to apply a fade effect to your text, enhancing its visual appeal. You can choose from various fade types.
```
faded_text = cli.fadet("Hello, fading world!", fadetype="purplepink")
print(faded_text)
```

The data_table function formats data into a table, making it easy to read and understand. You can specify headers, the display of indices, and the table format.
```
data = {
    'Apple': [10, 15],
    'Banana': [20, 25],
    'Cherry': [30, 35]
}

table_output = cli.data_table(data, headers=['Fruit', 'Quantity', 'Cost'])
print(table_output)
```

heres a good example on how these mix to create good looking ui elements for the console
```
import clui.index as cli

# Clear the console (optional)
cli.clear_console()

# Create fire-faded ASCII art with the "blood" font
text = "Hello world"
ascii_art = cli.ascii(text, font='bloody')
faded_ascii_art = cli.fadet(ascii_art, fadetype='purplepink')

# Print the result
print(faded_ascii_art)
```

big thanks too venaxyt for creating fade. the color gradient tool used in this repo
note: you can find all working color schemes for the fadet function at https://github.com/venaxyt/fade
