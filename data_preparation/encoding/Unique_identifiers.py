# Importing the CSV file
data = pd.read_csv('/mnt/data/horley_encoding.csv')

# Prepare an extended list of unique non-Latin characters from Greek and Cyrillic alphabets
non_latin_chars = [
    'α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω',
    'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я',
    'τ', 'в', 'С', 'Н', 'Γ', 'Π', 'Ц', 'р', 'ν', 'У', 'ь', 'З', 'Ξ', 'т', 'Χ', 'э', 'Φ', 'Κ', 'п', 'Μ', 'Ρ', 'Т', 'о', 'ϒ', 'Η', 'γ', 'и', 'Β', 'с', 'α', 'ъ', 'Й', 'Ι',
    'л', 'д', 'г', 'ψ', 'Ъ', 'Δ', 'а', 'Υ', 'Д', 'Ν', 'ю', 'ж', 'π', 'Л', 'у', 'я', 'Ζ', 'Щ', 'ф', 'ς', 'ξ', 'ο', 'Θ', 'е', 'μ', 'П', 'υ', 'м', 'Ε', 'χ', 'Ы', 'λ', 'Ч', 'й',
    'ω', 'ι', 'В', 'ц', 'κ', 'Я', 'б', 'О', 'М', 'Λ', 'Ж', 'Ю', 'Э', 'з', 'х', 'Е', 'Р', 'н', 'ы', 'Ь', 'β', 'И', 'θ', 'Х', 'Σ', 'Ψ', 'ч', 'Ш', 'щ', 'φ', 'к', 'ε', 'Ф', 'η',
    'Г', 'ζ', 'К', 'ш', 'Ο'
]

# Function to replace each question mark with a unique non-Latin character
def replace_question_marks(row):
    global non_latin_chars_index
    new_row = ''
    for char in row:
        if char == '?':
            new_row += non_latin_chars[non_latin_chars_index % len(non_latin_chars)]
            non_latin_chars_index += 1
        else:
            new_row += char
    return new_row

# Initialize index for non-Latin characters list
non_latin_chars_index = 0

# Apply the function to each column in the dataframe
for col in data.columns:
    data[col] = data[col].astype(str).apply(replace_question_marks)

# Save the modified dataframe to a new CSV file
final_output_file_path = '/mnt/data/final_modified_horley_encoding.csv'
data.to_csv(final_output_file_path, index=False)

final_output_file_path

